from app.ipabusers.models.category import Category
from django.core.validators import validate_ipv4_address
from django.core.exceptions import ValidationError
from app.utils.telegram.general import get_parameters
from telegram import InlineKeyboardButton, ParseMode, InlineKeyboardMarkup
from app.utils.telegram import Update, CallbackContext, trans as _
from ..bot_config.conversation_states_constants import SET_IP


class NewReport:
    def start(self, update: Update, context: CallbackContext) -> str:
        keyboard = [
            [
                InlineKeyboardButton(text=_("back_in_history_btn"), callback_data="start"),
            ]
        ]
        update.effective_message.edit_text(
            _("new_report_set_ip"),
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return SET_IP

    def save_ip(self, update: Update, context: CallbackContext) -> str:
        ip = update.effective_message.text
        try:
            validate_ipv4_address(ip)
            context.user_data["new_report"] = {"ip": ip}
            categories = Category.objects.all()
            keyboard = [
                [InlineKeyboardButton(text=item.name, callback_data=f"set_category {item.id}")] for item in categories
            ]
            update.effective_message.reply_text(
                _("new_report_set_category"),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(keyboard),
            )
        except ValidationError:
            update.effective_message.reply_text(_("new_report_ivalid_ip"))

    def set_category(self, update: Update, context: CallbackContext) -> int:
        category_id = get_parameters(update.callback_query.data)[0]
        print(category_id)
        keyboard = [
            [
                InlineKeyboardButton(text=_("go_to_start"), callback_data="start"),
            ]
        ]
        update.effective_message.reply_text(
            _("new_report_end") % ("1.0.0.2", "403"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
