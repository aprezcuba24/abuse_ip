from django.utils.translation import gettext_lazy as _
from ..handlers import start_manager

private_commands = {
    "start": {
        "callback": (start_manager, "command"),
        "description": _("start_command_description"),
    },
}
