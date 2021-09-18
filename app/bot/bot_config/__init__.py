from app.utils.telegram import BotManager
from .commands import private_commands


class ConfigBotManager(BotManager):
    def get_private_commands_config(self):
        return private_commands
