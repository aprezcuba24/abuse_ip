from app.users.models import User
from app.ipabusers.models.category import Category
from app.ipabusers.models.ipabusers import IpAbusers
from django.db.models import ForeignKey, ManyToManyField, CASCADE, SET_NULL
from app.utils.models import BaseModel


class IpCategory(BaseModel):
    ip = ForeignKey(IpAbusers, related_name="categories", on_delete=CASCADE)
    category = ForeignKey(Category, related_name="ips", on_delete=CASCADE)
    reported_by = ForeignKey(User, related_name="ips", on_delete=SET_NULL, null=True)
    users = ManyToManyField(User, related_name="ips_by_categories")
