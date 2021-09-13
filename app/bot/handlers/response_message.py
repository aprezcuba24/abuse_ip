from app.utils.telegram import Update, CallbackContext


def new_message(update: Update, context: CallbackContext):
    update.message.reply_text("Response")
