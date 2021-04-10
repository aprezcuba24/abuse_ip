from django.db.models import CharField
from django.db.models.fields import TextField
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel


class Category(BaseModel):
    name = CharField(_("Category"), max_length=255)
    code = CharField(_("Code"), max_length=255)
    description = TextField(_("Description"), max_length=255)

    def __str__(self) -> str:
        return self.name
