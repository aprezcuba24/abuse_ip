from ..handlers import start_manager, list_manager, my_list_manager, show_manager


callback_query_handlers = {
    "start": (start_manager, "callback"),
    "last_report": (list_manager, "callback"),
    "navigate_last_report": (list_manager, "navigate"),
    "my_reports": (my_list_manager, "callback"),
    "navigate_my_reports": (my_list_manager, "navigate"),
    "show_ip": (show_manager, "callback"),
}
