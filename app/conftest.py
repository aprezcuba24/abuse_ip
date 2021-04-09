import pytest

from app.users.models import User
from app.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture()
def api_client(db, user):
    """A Django test client logged in as an admin user."""
    from django.test.client import Client

    client = Client()
    return client
