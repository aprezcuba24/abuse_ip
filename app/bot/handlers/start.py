from app.utils.telegram import Update, CallbackContext


class StartManager:
    def command(self, update: Update, context: CallbackContext):
        update.effective_message.reply_text(**self._process_message(update, context))

    def callback(self, update: Update, context: CallbackContext):
        update.effective_message.edit_text(**self._process_message(update, context))

    def _process_message(self, update: Update, context: CallbackContext):
        return {"text": "start message"}
