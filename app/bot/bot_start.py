from app.bot.handlers.response_message import new_message
import telegram
from queue import Queue
from django.conf import settings
from telegram.ext import Dispatcher, MessageHandler, Filters, ContextTypes
from app.utils.telegram import CallbackContext
from app.bot.handlers.error import error_handler

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=Queue(), context_types=ContextTypes(context=CallbackContext))
dispatcher.add_handler(MessageHandler(Filters.text, new_message))
dispatcher.add_error_handler(error_handler)
