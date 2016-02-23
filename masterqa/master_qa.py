import ipdb
import os
import shutil
import sys
import time
from seleniumbase import BaseCase
from selenium.webdriver.remote.errorhandler import NoAlertPresentException
from style_sheet import style
import master_settings

LATEST_REPORT_DIR = "latest_report"
ARCHIVE_DIR = "report_archives"
RESULTS_PAGE = "results.html"
BAD_PAGE_LOG = "results_table.csv"
DEFAULT_VALIDATION_MESSAGE = master_settings.DEFAULT_VALIDATION_MESSAGE
WAIT_TIME_BEFORE_VERIFY = master_settings.WAIT_TIME_BEFORE_VERIFY

# This tool allows testers to quickly verify pages while assisted by automation


class __MasterQATestCase__(BaseCase):

    def get_timestamp(self):
        return str(int(time.time() * 1000))

    def manual_check_setup(self):
        self.manual_check_count = 0
        self.manual_check_successes = 0
        self.incomplete_runs = 0
        self.page_results_list = []
        self.clear_out_old_logs(archive_past_runs=False)

    def clear_out_old_logs(self, archive_past_runs=True, get_log_folder=False):
        abs_path = os.path.abspath('.')
        file_path = abs_path + "/%s" % LATEST_REPORT_DIR
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        if archive_past_runs:
            archive_timestamp = int(time.time())
            if not os.path.exists("%s/../%s/" % (file_path, ARCHIVE_DIR)):
                os.makedirs("%s/../%s/" % (file_path, ARCHIVE_DIR))
            archive_dir = "%s/../%s/log_%s" % (
                file_path, ARCHIVE_DIR, archive_timestamp)
            shutil.move(file_path, archive_dir)
            os.makedirs(file_path)
            if get_log_folder:
                return archive_dir
        else:
            # Just delete bad pages to make room for the latest run.
            filelist = [f for f in os.listdir(
                "./%s" % LATEST_REPORT_DIR) if f.startswith("failed_") or (
                f == RESULTS_PAGE) or (f.startswith("automation_failure")) or (
                f == BAD_PAGE_LOG)]
            for f in filelist:
                os.remove("%s/%s" % (file_path, f))

    def manual_page_check(self, *args):
        if not args:
            instructions = DEFAULT_VALIDATION_MESSAGE
        else:
            instructions = str(args[0])

        # Give the human enough time to see the page first
        time.sleep(WAIT_TIME_BEFORE_VERIFY)
        question = "Approve?"
        if instructions and "?" not in instructions:
            question = instructions + " Approve?"
        elif instructions and "?" in instructions:
            question = instructions

        if self.browser == 'ie':
            text = self.execute_script(
                '''if(confirm("%s")){return "Success!"}
                else{return "Failure!"}''' % question)
        else:
            self.execute_script('''if(confirm("%s")){window.alert("Success!")}
                else{window.alert("Failure!")}''' % question)
            time.sleep(0.05)
            self.wait_for_special_alert_absent()
            text = self.wait_for_and_accept_alert()
        self.manual_check_count += 1
        if "Success!" in text:
            self.manual_check_successes += 1
            self.page_results_list.append(
                '"%s","%s","%s","%s","%s","%s","%s","%s"' % (
                    self.manual_check_count,
                    "Success",
                    "-",
                    self.driver.current_url,
                    self.browser,
                    self.get_timestamp()[:-3],
                    instructions,
                    "*"))
            return 1
        else:
            bad_page_name = "failed_check_%s.jpg" % self.manual_check_count
            self.save_screenshot(bad_page_name, folder=LATEST_REPORT_DIR)
            self.page_results_list.append(
                '"%s","%s","%s","%s","%s","%s","%s","%s"' % (
                    self.manual_check_count,
                    "FAILED!",
                    bad_page_name,
                    self.driver.current_url,
                    self.browser,
                    self.get_timestamp()[:-3],
                    instructions,
                    "*"))
            return 0

    def wait_for_special_alert_absent(self, timeout=300):
        for x in range(int(timeout * 20)):
            try:
                alert = self.driver.switch_to_alert()
                dummy_variable = alert.text  # Raises exception if no alert
                if "?" not in dummy_variable:
                    return
                time.sleep(0.05)
            except NoAlertPresentException:
                return
        raise Exception(
            "%s seconds passed without human action! Stopping..." % timeout)

    def add_failure(self, exception=None):
        exc_info = None
        if exception:
            if hasattr(exception, 'msg'):
                exc_info = exception.msg
            elif hasattr(exception, 'message'):
                exc_info = exception.message
            else:
                exc_info = '(Unknown Exception)'

        self.incomplete_runs += 1
        error_page = "automation_failure_%s.jpg" % self.incomplete_runs
        self.save_screenshot(error_page, folder=LATEST_REPORT_DIR)
        self.page_results_list.append(
            '"%s","%s","%s","%s","%s","%s","%s","%s"' % (
                "ERR",
                "ERROR!",
                error_page,
                self.driver.current_url,
                self.browser,
                self.get_timestamp()[:-3],
                "-",
                exc_info))
        try:
            # Return to the original window if another was opened
            self.driver.switch_to_window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])
        except Exception:
            pass

    def add_bad_page_log_file(self):
        abs_path = os.path.abspath('.')
        file_path = abs_path + "/%s" % LATEST_REPORT_DIR
        log_file = "%s/%s" % (file_path, BAD_PAGE_LOG)
        f = open(log_file, 'w')
        h_p1 = '''"Num","Result","Screenshot","URL","Browser","Epoch Time",'''
        h_p2 = '''"Verification Instructions","Additional Info"\n'''
        page_header = h_p1 + h_p2
        f.write(page_header)
        for line in self.page_results_list:
            f.write("%s\n" % line)
        f.close()

    def add_results_page(self, html):
        abs_path = os.path.abspath('.')
        file_path = abs_path + "/%s" % LATEST_REPORT_DIR
        results_file_name = RESULTS_PAGE
        results_file = "%s/%s" % (file_path, results_file_name)
        f = open(results_file, 'w')
        f.write(html)
        f.close()
        return results_file

    def process_manual_check_results(self):
        perfection = True
        failures_count = self.manual_check_count - self.manual_check_successes
        if self.manual_check_successes == self.manual_check_count:
            pass
        else:
            print "WARNING!!! Page issues were detected by humans!"
            perfection = False

        if self.incomplete_runs > 0:
            print "WARNING!!! Not all tests finished running!"
            perfection = False

        if perfection:
            print "Success!!! All pages are good!"
        else:
            pass
        self.add_bad_page_log_file()  # Includes successful results

        log_string = self.clear_out_old_logs(get_log_folder=True)
        log_folder = log_string.split('/')[-1]
        abs_path = os.path.abspath('.')
        file_path = abs_path + "/%s" % ARCHIVE_DIR
        log_path = "%s/%s" % (file_path, log_folder)
        web_log_path = "file://%s" % log_path

        tf_color = "#11BB11"
        if failures_count > 0:
            tf_color = "#EE3A3A"

        ir_color = "#11BB11"
        if self.incomplete_runs > 0:
            ir_color = "#EE3A3A"

        new_data = '''<div><table><thead><tr><th>TEST REPORT SUMMARY
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              </th><th></th></tr></thead><tbody>
              <tr style="color:#00BB00"><td>CHECKS PASSED: <td>%s</tr>
              <tr style="color:%s"><td>CHECKS FAILED: <td>%s</tr>
              <tr style="color:#4D4DDD"><td>TOTAL VERIFICATIONS: <td>%s</tr>
              <tr style="color:%s"><td>INCOMPLETE TEST RUNS: <td>%s</tr>
              </tbody></table>''' % (self.manual_check_successes,
                                     tf_color,
                                     failures_count,
                                     self.manual_check_count,
                                     ir_color,
                                     self.incomplete_runs)

        new_view_1 = '''<h1 id="ContextHeader" class="sectionHeader" title="">
                     %s</h1>''' % new_data

        log_link_shown = '../%s%s/' % (
            ARCHIVE_DIR, web_log_path.split(ARCHIVE_DIR)[1])
        csv_link = '%s/%s' % (web_log_path, BAD_PAGE_LOG)
        csv_link_shown = '%s' % BAD_PAGE_LOG
        new_view_2 = '''<p><p><p><p><h2><table><tbody>
            <tr><td>LOG FILES LINK:&nbsp;&nbsp;<td><a href="%s">%s</a></tr>
            <tr><td>RESULTS TABLE:&nbsp;&nbsp;<td><a href="%s">%s</a></tr>
            </tbody></table></h2><p><p><p><p>''' % (
            web_log_path, log_link_shown, csv_link, csv_link_shown)

        new_view_3 = '<h2><table><tbody></div>'
        any_screenshots = False
        for line in self.page_results_list:
            line = line.split(',')
            if line[1] == '"FAILED!"' or line[1] == '"ERROR!"':
                if not any_screenshots:
                    any_screenshots = True
                    new_view_3 += '''<thead><tr><th>SCREENSHOT FILE
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </th><th>LOCATION OF FAILURE</th></tr></thead>'''
                line = '<a href="%s">%s</a>' % (
                    "file://" + log_path + '/' + line[2], line[2]) + '''
                    &nbsp;&nbsp;<td>
                    ''' + '<a href="%s">%s</a>' % (line[3], line[3])
                line = line.replace('"', '')
                new_view_3 += '<tr><td>%s</tr>\n' % line
        new_view_3 += '</tbody></table>'
        new_view_4 = '''<h2 style="color:#0C8CDB; font-size:27px;">
            *** Powered by SeleniumBase ***</h2>'''
        new_view = '%s%s%s%s' % (
            new_view_1, new_view_2, new_view_3, new_view_4)
        results_content = '<body>%s</body>' % new_view
        new_source = '<html><head>%s</head>%s</html>' % (
            style, results_content)
        results_file = self.add_results_page(new_source)
        archived_results_file = log_path + '/' + RESULTS_PAGE
        shutil.copyfile(results_file, archived_results_file)
        print "Results located at: " + results_file
        self.open("file://%s" % archived_results_file)
        ipdb.set_trace()


class MasterQA(__MasterQATestCase__):

    def setUp(self):
        super(__MasterQATestCase__, self).setUp()
        self.manual_check_setup()

    def verify(self, *args):
        self.manual_page_check(*args)

    def tearDown(self):
        if sys.exc_info()[1]:
            self.add_failure(sys.exc_info()[1])
        self.process_manual_check_results()
        super(__MasterQATestCase__, self).tearDown()