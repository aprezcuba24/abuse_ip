from ..handlers import start_manager


callback_query_handlers = {
    "start": (start_manager, "callback"),
}
