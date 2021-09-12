from app.ipabusers.api.ipabusers import IpAbuserViewSet
from app.ipabusers.api.category import CategoryViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url, include
from django.urls import path
from app.bot.web_hook import TelegramWebhook

from app.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("ips", IpAbuserViewSet)


app_name = "api"
urlpatterns = [
    url(r"^", include(router.urls)),
    path("telegram-webhook/<str:pk>/", TelegramWebhook.as_view(), name="telegram-webhook"),
]
