import emoji
from django.utils.translation import gettext_lazy


def trans(*args, **kwargs):
    return emoji.emojize(str(gettext_lazy(*args, **kwargs)), use_aliases=True)
