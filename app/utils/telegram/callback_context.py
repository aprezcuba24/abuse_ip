from telegram.ext import CallbackContext as BaseCallbackContext
from app.users.models import User


class CallbackContext(BaseCallbackContext):
    @property
    def user_model(self) -> User:
        update = self._update
        try:
            user = User.objects.get(external_id=update.effective_user.id)
        except User.DoesNotExist:
            user = User(external_id=update.effective_user.id)
        user_data = update.effective_user
        user.username = user_data["id"]
        user.external_id = user_data["id"]
        user.is_bot = user_data["is_bot"]
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.chat_id = update.effective_chat.id
        user.save()
        return user
