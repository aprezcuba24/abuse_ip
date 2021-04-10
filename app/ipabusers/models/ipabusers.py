from django.db.models import CharField, QuerySet
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel


class ManagerQuerySet(QuerySet):
    pass


class IpAbusers(BaseModel):
    ip = CharField(_("Ip address"), max_length=255)

    objects = ManagerQuerySet.as_manager()

    def __str__(self) -> str:
        return self.ip
