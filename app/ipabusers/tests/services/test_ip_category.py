from app.ipabusers.factories import CategoryFactory
import pytest
from app.ipabusers.models.ip_category import IpCategory
from app.ipabusers.models.ipabusers import IpAbusers
from app.ipabusers.services.ip_category import IpCategoryService


@pytest.mark.django_db
def test_create(user):
    category = CategoryFactory()
    assert len(IpAbusers.objects.all()) == 0
    assert len(IpCategory.objects.all()) == 0
    IpCategoryService.create(ip="10.0.0.1", reported_by=user, category=category)
    assert len(IpAbusers.objects.all()) == 1
    assert len(IpCategory.objects.all()) == 1
