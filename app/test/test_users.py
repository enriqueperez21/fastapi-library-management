import pytest

valid_user = {
    "name": "Test User",
    "email": "test@mail.com",
    "password": "Strong@123"
}


def test_post_user(client):
    response = client.post("/users", json=valid_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@mail.com"
    assert "id" in data


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 404

    client.post("/users", json=valid_user)
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Test User"
    assert response.json()[0]["email"] == "test@mail.com"
    assert isinstance(response.json(), list)



def test_get_user(client):
    response = client.get(f"/users/1")
    assert response.status_code == 404

    response = client.post("/users", json=valid_user)
    user_id = response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@mail.com"


def test_get_user_by_email(client):
    response = client.get("/users/by-email?email=test@mail.com")
    assert response.status_code == 404

    response = client.post("/users", json=valid_user)
    user_id = response.json()["id"]

    response = client.get("/users/by-email?email=test@mail.com")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "Test User"
    assert data["email"] == "test@mail.com"


def test_update_user(client):
    response = client.post("/users", json=valid_user)
    user_id = response.json()["id"]

    response = client.patch(f"/users/{user_id}", json={"name": "Updated User"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated User"

    response = client.patch(f"/users/{user_id}", json={"email": "test@mail.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@mail.com"

    response = client.patch(f"/users/{user_id}", json={"password": "@123Strong"})
    assert response.status_code == 200


def test_delete_user(client):
    response = client.delete(f"/users/1")
    assert response.status_code == 404

    response = client.post("/users", json=valid_user)
    user_id = response.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404


def assert_error_values_msg(responses, msgs):
    for response, expected_msg in zip(responses, msgs):
        assert response.status_code == 422
        assert expected_msg in response.json()["detail"][0]["msg"]

@pytest.mark.parametrize("invalid_user", [
    {"name": "Test User", "password": "Strong@123"},
    {"name": "Test User","email": "test@mail.com"},
    {"password": "Strong@123"},
])
def test_create_user_invalid(client, invalid_user):
    response = client.post("/users", json=invalid_user)
    assert response.status_code == 422


@pytest.mark.parametrize("password, expected_msg", [
    ("strong", "String should have at least 8 characters"),
    ("stroooong", "Value error, Password must contain at least one uppercase letter"),
    ("stroooongS", "Value error, Password must contain at least one number"),
    ("stroooongS1", "Value error, Password must contain at least one special character (@$!%*?&.)"),
])
def test_update_user_invalid_passwords(client, password, expected_msg):
    user_id = client.post("/users", json=valid_user).json()["id"]
    response = client.patch(f"/users/{user_id}", json={"password": password})
    assert response.status_code == 422
    assert expected_msg in response.json()["detail"][0]["msg"]