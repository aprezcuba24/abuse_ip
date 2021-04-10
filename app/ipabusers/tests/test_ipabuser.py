from app.ipabusers.models.ip_category import IpCategory
from app.ipabusers.models.ipabusers import IpAbusers
from app.ipabusers.factories import CategoryFactory, IpAbusersFactory


def test_ip_list(bot_client):
    IpAbusersFactory()
    IpAbusersFactory()
    response = bot_client.get("/api/ips/")
    assert response.status_code == 200
    assert len(response.data["results"]) == 2


def test_ip_get(bot_client):
    ip = IpAbusersFactory(ip="10.0.0.1")
    response = bot_client.get(f"/api/ips/{str(ip.id)}/")
    assert response.status_code == 200
    assert response.data["ip"] == "10.0.0.1"


def test_ip_create(bot_client):
    category = CategoryFactory()
    assert len(IpAbusers.objects.all()) == 0
    assert len(IpCategory.objects.all()) == 0
    response = bot_client.post("/api/ips/", data={"ip_address": "10.0.0.1", "category": str(category.id)})
    assert response.status_code == 201
    assert IpAbusers.objects.filter(ip="10.0.0.1").exists()
    assert IpCategory.objects.filter(ip__ip="10.0.0.1", category=category).exists()


def test_ip_already_exists(bot_client):
    category = CategoryFactory()
    IpAbusersFactory(ip="10.0.0.1")
    assert len(IpAbusers.objects.all()) == 1
    assert len(IpCategory.objects.all()) == 0
    response = bot_client.post("/api/ips/", data={"ip_address": "10.0.0.1", "category": str(category.id)})
    assert response.status_code == 201
    assert IpCategory.objects.filter(ip__ip="10.0.0.1", category=category).exists()
    assert len(IpAbusers.objects.all()) == 1
