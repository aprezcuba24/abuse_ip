from app.utils.telegram import Update, CallbackContext
from app.utils.telegram import trans as _
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class StartManager:
    def command(self, update: Update, context: CallbackContext):
        update.effective_message.reply_text(**self._process_message(update, context))

    def callback(self, update: Update, context: CallbackContext):
        update.effective_message.edit_text(**self._process_message(update, context))

    def _process_message(self, update: Update, context: CallbackContext):
        keyboard = [
            [
                InlineKeyboardButton(text=str(_("start_last_report")), callback_data="last_report"),
            ],
            [
                InlineKeyboardButton(text=str(_("start_my_reports")), callback_data="my_reports"),
            ],
            [
                InlineKeyboardButton(text=str(_("start_new_report")), callback_data="new_report"),
            ],
        ]
        return {"text": str(_("start_header")), "reply_markup": InlineKeyboardMarkup(keyboard)}
