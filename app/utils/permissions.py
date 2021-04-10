import json
from rest_framework.permissions import BasePermission
from django.conf import settings


class IsBotPermission(BasePermission):
    def has_permission(self, request, view):
        data = json.loads(request.META.get("HTTP_AUTHORIZATION"))
        return "app_key" in data and settings.BOT_SECRET_KEY == data["app_key"]
