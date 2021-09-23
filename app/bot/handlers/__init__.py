from .start import StartManager
from .new_report import NewReport
from .error import error_handler  # noqa
from .ip_list import IpListManager

start_manager = StartManager()
new_report_manager = NewReport()
list_manager = IpListManager()
