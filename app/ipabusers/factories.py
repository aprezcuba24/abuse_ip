from app.users.tests.factories import UserFactory
from factory.django import DjangoModelFactory
import factory
from . import models


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Faker("last_name")
    code = factory.Faker("last_name")
    description = factory.Faker("last_name")


class IpAbusersFactory(DjangoModelFactory):
    class Meta:
        model = models.IpAbusers

    ip = factory.Faker("ipv4")


class IpCategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.IpCategory

    category = factory.SubFactory(CategoryFactory)
    reported_by = factory.SubFactory(UserFactory)
    ip = factory.SubFactory(IpAbusersFactory)
