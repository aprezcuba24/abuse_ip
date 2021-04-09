from app.ipabusers.factories import IpAbusersFactory


def test_ip_list(api_client):
    IpAbusersFactory()
    IpAbusersFactory()
    response = api_client.get("/api/ips/")
    assert response.status_code == 200
    assert len(response.data["results"]) == 2


def test_ip_get(api_client):
    ip = IpAbusersFactory(ip="10.0.0.1")
    response = api_client.get(f"/api/ips/{str(ip.id)}/")
    assert response.status_code == 200
    assert response.data["ip"] == "10.0.0.1"
