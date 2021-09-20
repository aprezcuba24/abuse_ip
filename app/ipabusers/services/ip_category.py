from app.ipabusers.models.ip_category import IpCategory
from app.ipabusers.models.ipabusers import IpAbusers


class IpCategoryService:
    @classmethod
    def create(cls, ip, reported_by, category):
        ip_entity, _ = IpAbusers.objects.get_or_create(ip=ip)
        try:
            ip_category = IpCategory.objects.get(ip=ip_entity, category=category)
        except IpCategory.DoesNotExist:
            ip_category = IpCategory(ip=ip_entity, category=category, reported_by=reported_by)
            ip_category.save()
        ip_category.users.add(reported_by)
        return ip_category
