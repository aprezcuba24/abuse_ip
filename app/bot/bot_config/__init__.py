from app.utils.telegram import BotManager
from ..handlers import error_handler
from .commands import private_commands
from .callback_query_handlers import callback_query_handlers
from .conversation import new_report


class ConfigBotManager(BotManager):
    def _start_init(self):
        super()._start_init()
        self.dispatcher.add_error_handler(error_handler)

    def get_private_commands_config(self):
        return private_commands

    def get_callback_query_handlers_config(self):
        return callback_query_handlers

    def get_conversations_config(self):
        return [new_report]
