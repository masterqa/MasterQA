from masterqa import MasterQA


class MasterQATests(MasterQA):

    def test_results_page_only(self):
        ''' Importing MasterQA should take you to the results
        page at the end of the test, even if testing nothing. '''
        self.auto_close_results()
