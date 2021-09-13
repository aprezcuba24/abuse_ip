from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from app.utils.telegram import Update
from .bot_start import bot, dispatcher


class TelegramWebhook(APIView):
    permission_classes = []

    def post(self, request, pk, format=None):
        if settings.TELEGRAM_TOKEN != pk:
            return Http404()
        update = Update.de_json(request.data, bot)
        dispatcher.process_update(update=update)
        return Response()
