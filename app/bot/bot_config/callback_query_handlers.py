from ..handlers import start_manager, list_manager


callback_query_handlers = {
    "start": (start_manager, "callback"),
    "last_report": (list_manager, "callback"),
    "navigate_last_report": (list_manager, "navigate"),
}
