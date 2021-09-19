from telegram.ext import Filters
from ..handlers import new_report_manager
from . import conversation_states_constants as constants

new_report = {
    "entry_points": {
        "callback_query_handlers": {
            "new_report": (new_report_manager, "start"),
            "set_category": (new_report_manager, "set_category"),
        }
    },
    "states": {
        constants.SET_IP: {
            "callback": (new_report_manager, "save_ip"),
            "filters": Filters.text,
        }
    },
}
