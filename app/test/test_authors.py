import pytest
from app.test.author_data import valid_author, invalid_author_create_inputs, invalid_author_update_inputs


@pytest.fixture
def created_author(client):
    return client.post("/authors", json=valid_author).json()


def test_post(client):
    response = client.post("/authors", json=valid_author)
    assert response.status_code == 201
    data = response.json()
    assert data["name"]      == valid_author["name"]
    assert data["birthdate"] == valid_author["birthdate"]
    assert "id" in data


def test_get_all(client, created_author):
    response = client.get("/authors")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"]      == valid_author["name"]
    assert data[0]["birthdate"] == valid_author["birthdate"]
    assert data[0]["id"]        == created_author["id"]
    assert isinstance(response.json(), list)


def test_get(client, created_author):
    response = client.get(f"/authors/{created_author['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"]      == valid_author["name"]
    assert data["birthdate"] == valid_author["birthdate"]


def test_update_name(client, created_author):
    response = client.patch(f"/authors/{created_author['id']}", json={"name": "Updated Author"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Author"


def test_update_birthdate(client, created_author):
    response = client.patch(f"/authors/{created_author['id']}", json={"birthdate": "21/11/2000"})
    assert response.status_code == 200
    assert response.json()["birthdate"] == "21/11/2000"


def test_delete(client, created_author):
    response = client.delete(f"/authors/{created_author['id']}")
    assert response.status_code == 204

    response = client.get(f"/authors/{created_author['id']}")
    assert response.status_code == 404


def test_get_all_not_found(client):
    response = client.get("/authors")
    assert response.status_code == 404


def test_get_not_found(client):
    response = client.get(f"/authors/1")
    assert response.status_code == 404
 

def test_update_not_found(client):
    response = client.patch(f"/authors/1", json={"name": "Updated Author"})
    assert response.status_code == 404


def test_delete_not_found(client):
    response = client.delete(f"/authors/1")
    assert response.status_code == 404


@pytest.mark.parametrize("invalid_author", invalid_author_create_inputs)
def test_post_invalid(client, invalid_author):
    response = client.post("/authors", json=invalid_author["input"])
    assert response.status_code == 422
    assert invalid_author["msg"] in response.json()["detail"][0]["msg"]


@pytest.mark.parametrize("invalid_author_update", invalid_author_update_inputs)
def test_update_invalid(client, created_author, invalid_author_update):
    response = client.patch(f"/authors/{created_author['id']}", json={"birthdate": invalid_author_update["birthdate"]})
    assert response.status_code == 422
    assert invalid_author_update["msg"] in response.json()["detail"][0]["msg"]