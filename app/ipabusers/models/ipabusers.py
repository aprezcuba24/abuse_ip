from django.core.validators import validate_ipv46_address
from django.db.models import CharField, QuerySet
from django.utils.translation import gettext_lazy as _
from app.utils.models import BaseModel
from app.users.models import User


class ManagerQuerySet(QuerySet):
    def get_by_user(self, user: User):
        return self.filter(categories__users=user).distinct("id")


class IpAbusers(BaseModel):
    ip = CharField(_("Ip address"), max_length=255, validators=[validate_ipv46_address])

    objects: ManagerQuerySet = ManagerQuerySet.as_manager()

    def __str__(self) -> str:
        return self.ip
