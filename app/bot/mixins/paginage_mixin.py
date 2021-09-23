from django.core.paginator import Paginator
from abc import ABCMeta, abstractmethod
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from app.bot.mixins.back_buttons_mixin import BackButtonsMixin
from typing import Any
from app.utils.telegram.general import get_parameters
from app.utils.telegram import trans as _
from app.utils.telegram import CallbackContext


class PaginateMixin(BackButtonsMixin, metaclass=ABCMeta):

    PAGE_SIZE = 5

    @abstractmethod
    def _get_item_command(self, item: Any, **kwargs):
        pass

    def _get_create_command(self, **kwargs):
        pass

    @abstractmethod
    def _get_list_header(self, **kwargs):
        pass

    @abstractmethod
    def _callback_subfix(self, **kwargs):
        pass

    def get_queryset(self, **kwargs):
        return self.queryset

    def callback(self, update: Update, context: CallbackContext):
        update.effective_message.edit_text(**self.paginate(update, context))

    def _list_out(self, **kwargs):
        return "start"

    def paginate(self, update: Update, context: CallbackContext):
        return self._list(page_number=1, update=update, context=context)

    def _button_item(self, item: Any):
        return InlineKeyboardButton(
            text=str(item),
            callback_data=self._get_item_command(item),
        )

    def _empty_list_text(self):
        return _("list_empty")

    def _list(self, page_number, update: Update, context: CallbackContext):
        paginator = Paginator(self.get_queryset(update=update, context=context), self.PAGE_SIZE)
        page = paginator.page(page_number)
        buttons = []
        if paginator.num_pages > 0:
            buttons += [[self._button_item(item)] for item in page.object_list]
        navigate = []
        if page.has_previous():
            navigate += [
                InlineKeyboardButton(
                    text=_("list_previous"),
                    callback_data=f"navigate_{self._callback_subfix()} {page_number - 1}",
                )
            ]
        if page.has_next():
            navigate += [
                InlineKeyboardButton(
                    text=_("list_next"),
                    callback_data=f"navigate_{self._callback_subfix()} {page_number + 1}",
                )
            ]
        if len(navigate):
            buttons += [navigate]
        buttons += self._extra_buttons(context=context, update=update)
        if not buttons:
            return {"text": self._empty_list_text()}
        return {
            "text": self._get_list_header(context=context, update=update, paginator=paginator, page=page),
            "reply_markup": InlineKeyboardMarkup(buttons),
            "parse_mode": ParseMode.MARKDOWN,
        }

    def _create_button(self, context: CallbackContext):
        create_command = self._get_create_command(context=context)
        if create_command:
            return InlineKeyboardButton(
                text=_("list_create"),
                callback_data=self._get_create_command(context=context),
            )

    def _extra_buttons(self, update: Update, context: CallbackContext):
        command_back = self._list_out(context=context)
        buttons = []
        button_create = self._create_button(context=context)
        if button_create:
            buttons += [[button_create]]
        buttons += [self._get_back_buttons(command_back=command_back)]
        return buttons

    def navigate(self, update: Update, context: CallbackContext):
        params = get_parameters(update.callback_query.data)
        update.effective_message.edit_text(**self._list(update=update, context=context, page_number=int(params[0])))
