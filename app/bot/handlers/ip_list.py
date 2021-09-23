from app.ipabusers.models.ipabusers import IpAbusers
from typing import Any
from app.bot.mixins.paginage_mixin import PaginateMixin
from app.utils.telegram import trans as _


class IpListManager(PaginateMixin):
    queryset = IpAbusers.objects.order_by("-created_at")

    def _get_item_command(self, item: Any, **kwargs):
        return f"show_ip last_report {str(item.id)}"

    def _get_list_header(self, **kwargs):
        return _("last_report_header")

    def _callback_subfix(self, **kwargs):
        return "last_report"
