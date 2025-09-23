import pytest
from app.test.test_data import valid_user, invalid_user_create_inputs, invalid_user_passwords


@pytest.fixture
def created_user(client):
    return client.post("/users", json=valid_user).json()


#Test CRUD operations
def test_post(client):
    response = client.post("/users", json=valid_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == valid_user["name"]
    assert data["email"] == valid_user["email"]
    assert "id" in data


def test_get_all(client, created_user):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json()[0]["name"] == valid_user["name"]
    assert response.json()[0]["email"] == valid_user["email"]
    assert isinstance(response.json(), list)


def test_get(client, created_user):
    response = client.get(f"/users/{created_user['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == valid_user["name"]
    assert data["email"] == valid_user["email"]


def test_get_by_email(client, created_user):
    response = client.get(f"/users/by-email?email={valid_user['email']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_user["id"]
    assert data["name"] == valid_user["name"]
    assert data["email"] == valid_user["email"]


def test_update_name(client, created_user):
    response = client.patch(f"/users/{created_user['id']}", json={"name": "Updated User"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"


def test_update_email(client, created_user):
    response = client.patch(f"/users/{created_user['id']}", json={"email": "test2@mail.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "test2@mail.com"


def test_update_password(client, created_user):
    response = client.patch(f"/users/{created_user['id']}", json={"password": "@123Strong"})
    assert response.status_code == 200


def test_delete(client, created_user):
    response = client.delete(f"/users/{created_user['id']}")
    assert response.status_code == 204

    response = client.get(f"/users/{created_user['id']}")
    assert response.status_code == 404


#Test not found errors
def test_get_all_not_found(client):
    response = client.get("/users")
    assert response.status_code == 404


def test_get_not_found(client):
    response = client.get(f"/users/1")
    assert response.status_code == 404


def test_get_by_email_not_found(client):
    response = client.get("/users/by-email?email=test@mail.com")
    assert response.status_code == 404
 

def test_update_not_found(client):
    response = client.patch(f"/users/1", json={"name": "Updated User"})
    assert response.status_code == 404


def test_delete_not_found(client):
    response = client.delete(f"/users/1")
    assert response.status_code == 404


#Test inputs errors
def test_post_duplicate(client, created_user):
    response = client.post("/users", json=valid_user)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_update_email_duplicate(client, created_user):
    client.post("/users", json={**valid_user, "email": "test_update@mail.com"})
    response = client.patch(f"/users/{created_user['id']}", json={"email": "test_update@mail.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


@pytest.mark.parametrize("invalid_user", invalid_user_create_inputs)
def test_post_missing_fields(client, invalid_user):
    response = client.post("/users", json=invalid_user)
    assert response.status_code == 422


@pytest.mark.parametrize("input", invalid_user_passwords)
def test_post_invalid_user_passwords(client, input):
    response = client.post("/users", json={**valid_user, "password": input["password"]})
    assert response.status_code == 422
    assert input["msg"] in response.json()["detail"][0]["msg"]


@pytest.mark.parametrize("input", invalid_user_passwords)
def test_update_invalid_user_passwords(client, input):
    user_id = client.post("/users", json=valid_user).json()["id"]
    response = client.patch(f"/users/{user_id}", json={"password": input["password"]})
    assert response.status_code == 422
    assert input["msg"] in response.json()["detail"][0]["msg"]