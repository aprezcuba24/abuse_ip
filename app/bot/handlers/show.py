from app.ipabusers.models.ipabusers import IpAbusers
from app.utils.telegram import Update, CallbackContext
from app.utils.telegram import trans as _
from telegram import InlineKeyboardMarkup
from app.bot.mixins.back_buttons_mixin import BackButtonsMixin
from app.utils.telegram.general import get_parameters


class ShowManager(BackButtonsMixin):
    def command(self, update: Update, context: CallbackContext):
        if len(context.args) == 0:
            return update.effective_message.reply_text(text=str(_("show_ip_set_ip_error")))
        ip = context.args[0]
        try:
            ip_object = IpAbusers.objects.get(ip=ip)
            update.effective_message.reply_text(**self._process_message(update, context, ip_object=ip_object))
        except IpAbusers.DoesNotExist:
            return update.effective_message.reply_text(text=str(_("show_ip_does_not_exist_error")) % ip)

    def callback(self, update: Update, context: CallbackContext):
        [command_back, id] = get_parameters(update.callback_query.data)
        ip_object = IpAbusers.objects.get(pk=id)
        update.effective_message.edit_text(
            **self._process_message(update, context, ip_object=ip_object, command_back=command_back)
        )

    def _process_message(self, update: Update, context: CallbackContext, ip_object, command_back=None):
        categories = " \n".join(
            [_("ip_category") % (item.category.name, item.category.code) for item in ip_object.categories.all()]
        )
        keyboard = [self._get_back_buttons(command_back=command_back)]
        return {
            "text": str(_("show_ip_header")) % (ip_object.ip, categories),
            "reply_markup": InlineKeyboardMarkup(keyboard),
        }
