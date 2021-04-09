from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel


class IpAbusers(BaseModel):
    ip = CharField(_("Ip address"), max_length=255)
