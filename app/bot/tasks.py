import time
from telegram.error import RetryAfter
from django.conf import settings
from django.urls import reverse
from config import celery_app
from .bot_start import bot


@celery_app.task(bind=True)
def start_bot(*args, **kwargs):
    if not settings.APP_HOST:
        return
    while True:
        try:
            url = settings.APP_HOST + reverse("api:telegram-webhook", args=[settings.TELEGRAM_TOKEN])
            s = bot.setWebhook(url)
            return "Webhook registered" if s else "Webhook error"
        except RetryAfter:
            time.sleep(10)  # Wait 10 secounds
            pass
