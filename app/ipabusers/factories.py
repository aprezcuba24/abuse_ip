from factory.django import DjangoModelFactory
import factory
from . import models


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Faker("last_name")
    code = factory.Faker("last_name")
    description = factory.Faker("last_name")
