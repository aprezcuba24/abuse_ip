from django.apps import AppConfig


class IpabusersConfig(AppConfig):
    name = "app.ipabusers"

    def ready(self):
        from app.bot.tasks import start_bot

        start_bot.apply_async()
