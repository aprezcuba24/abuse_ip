from typing import Tuple
from django.core.validators import validate_ipv46_address
from django.db.models import CharField, QuerySet
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel


class ManagerQuerySet(QuerySet):
    pass


class IpAbusers(BaseModel):
    ip = CharField(_("Ip address"), max_length=255, validators=[validate_ipv46_address])

    objects = ManagerQuerySet.as_manager()

    def __str__(self) -> str:
        return self.ip
