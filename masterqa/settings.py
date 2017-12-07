"""
MasterQA Settings

You'll probably want to customize this to your own environment and needs.
"""

# The default message that appears when you don't specify a custom message
DEFAULT_VALIDATION_MESSAGE = "Does the page look good?"

# The time delay (in seconds) before the validation pop-up appears
WAIT_TIME_BEFORE_VERIFY = 1.0

# If True, the automation will start in full-screen mode
START_IN_FULL_SCREEN_MODE = False

# The maximimum idle time allowed (in seconds) before timing out and exiting
MAX_IDLE_TIME_BEFORE_QUIT = 600

# Default names for folders and files saved
LATEST_REPORT_DIR = "latest_report"
REPORT_ARCHIVE_DIR = "archived_reports"
HTML_REPORT = "report.html"
RESULTS_TABLE = "results_table.csv"
