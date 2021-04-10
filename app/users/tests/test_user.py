from app.users.tests.factories import UserFactory
import json
from app.users.models import User


def test_user_create(api_client):
    assert len(User.objects.all()) == 1  # There is a user of conftest
    response = api_client.post(
        "/api/users/get-or-create/some_telegram_id/",
        data=json.dumps({"first_name": "first_name"}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert len(User.objects.all()) == 2
    assert User.objects.filter(first_name="first_name", external_id="some_telegram_id").exists()


def test_the_user_already_exists(api_client):
    UserFactory(external_id="some_telegram_id", first_name="first_name")
    assert len(User.objects.all()) == 2  # There is a user of conftest
    response = api_client.post(
        "/api/users/get-or-create/some_telegram_id/",
        data=json.dumps({"first_name": "first_name updated"}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert len(User.objects.all()) == 2
    assert User.objects.filter(first_name="first_name updated", external_id="some_telegram_id").exists()
