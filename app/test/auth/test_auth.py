import pytest
from app.test.conftest import *
from app.test.users.user_data import valid_user

detail_msg = {"detail": "Incorrect email or password"}

@pytest.fixture
def created_user(client):
    return client.post("/users", json=valid_user).json()

# Test authentication operations
def test_login(client, created_user):
    response = client.post("/auth/login", data=valid_user)
    assert_200(response)
    assert "access_token" in response.json()

# Test invalid login attempts
def test_login_nothing(client, created_user):
    assert_422(client.post("/auth/login", data={}))

def test_login_no_email(client, created_user):
    response = client.post("/auth/login", data={"email": "no_existe@mail.com", "password": valid_user["password"]})
    assert_401(response)
    assert_data_verification(response.json(), detail_msg, ["detail"])

def test_login_invalid_password(client, created_user):
    response = client.post("/auth/login", data={"email": valid_user["email"], "password": "12345"})
    assert_401(response)
    assert_data_verification(response.json(), detail_msg, ["detail"])