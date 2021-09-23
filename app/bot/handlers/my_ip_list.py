from app.ipabusers.models.ipabusers import IpAbusers
from typing import Any
from app.bot.mixins.paginage_mixin import PaginateMixin
from app.utils.telegram import trans as _
from app.utils.telegram import CallbackContext, Update


class MyIpListManager(PaginateMixin):
    def get_queryset(self, update: Update, context: CallbackContext):
        return IpAbusers.objects.get_by_user(context.user_model).order_by("id", "-created_at")

    def _get_item_command(self, item: Any, **kwargs):
        return f"show_ip {str(item.id)}"

    def _get_list_header(self, **kwargs):
        return _("my_reports_header")

    def _callback_subfix(self, **kwargs):
        return "my_reports"
