from app.ipabusers.factories import CategoryFactory


def test_categories_list(api_client):
    CategoryFactory()
    CategoryFactory()
    response = api_client.get("/api/categories/")
    assert response.status_code == 200
    assert len(response.data["results"]) == 2


def test_category_get(api_client):
    category = CategoryFactory(name="categiry 1")
    response = api_client.get(f"/api/categories/{str(category.id)}/")
    assert response.status_code == 200
    assert response.data["name"] == "categiry 1"
