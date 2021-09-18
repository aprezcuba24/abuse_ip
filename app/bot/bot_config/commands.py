from django.utils.translation import gettext_lazy as _
from ..handlers import start

private_commands = {
    "start": {
        "callback": (start, "command"),
        "description": _("start_command_description"),
    },
}
