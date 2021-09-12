import telegram
from rest_framework.response import Response
from rest_framework.views import APIView
from telegram.ext import Dispatcher, MessageHandler, Filters, ContextTypes
from app.utils.telegram import Update, CallbackContext
from queue import Queue
from django.conf import settings


class TelegramWebhook(APIView):
    permission_classes = []

    def post(self, request, pk, format=None):
        bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
        update = Update.de_json(request.data, bot)
        dispatcher = Dispatcher(bot=bot, update_queue=Queue(), context_types=ContextTypes(context=CallbackContext))
        dispatcher.add_handler(MessageHandler(Filters.text, self.new_message))
        dispatcher.add_error_handler(self.error_handler)

        dispatcher.process_update(update=update)
        return Response()

    def new_message(self, update: Update, context: CallbackContext):
        update.message.reply_text("Response")

    def error_handler(self, update, context):
        """
        Log the error in sentry
        """
        print(context.error)
