import telegram
from queue import Queue
from django.conf import settings
from telegram.ext import Dispatcher, ContextTypes
from app.utils.telegram import CallbackContext
from .bot_config import ConfigBotManager

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=Queue(), context_types=ContextTypes(context=CallbackContext))

bot_manager = ConfigBotManager(dispatcher=dispatcher, bot=bot)
bot_manager.bot.set_my_commands(commands=bot_manager.get_my_private_commands())
