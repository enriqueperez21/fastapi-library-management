import pytest
from app.test.conftest import *
from app.test.users.user_data import valid_user
from app.test.auth.auth_data import invalid_token

@pytest.fixture
def created_user(client): return client.post("/users", json=valid_user).json()

# Test authentication operations
def test_get_user(client, created_user):
    response = client.post("/auth/login", data=valid_user)
    token = response.json().get("access_token")
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert_200(response)
    assert_data_verification(response.json(), created_user, ["id", "name", "email"])

# Test invalid autentication
def test_get_user_invalid_token(client):
    response = client.get("/auth/me", headers={"Authorization": f"Bearer {invalid_token}"})
    assert_401(response)
    assert response.json().get("detail") == "Could not validate credentials"