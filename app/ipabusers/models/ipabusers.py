from typing import Tuple
from django.core.validators import validate_ipv46_address
from django.db.models import CharField, QuerySet
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel


class ManagerQuerySet(QuerySet):
    def get_or_create(self, *args, **kwargs) -> Tuple["IpAbusers", bool]:
        try:
            return self.get(**kwargs), False
        except IpAbusers.DoesNotExist:
            pass
        object = IpAbusers(**kwargs)
        object.full_clean()
        object.save()
        return object, True


class IpAbusers(BaseModel):
    ip = CharField(_("Ip address"), max_length=255, validators=[validate_ipv46_address])

    objects = ManagerQuerySet.as_manager()

    def __str__(self) -> str:
        return self.ip
