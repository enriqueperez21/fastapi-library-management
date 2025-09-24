import pytest
from app.test.conftest import *
from app.test.users.user_data import valid_user, invalid_user_create_inputs, invalid_user_passwords

@pytest.fixture
def created_user(client):
    return client.post("/users", json=valid_user).json()

#Test CRUD operations
def test_post(client):
    response = client.post("/users", json=valid_user)
    assert_201(response)
    assert "id" in response.json()
    assert_data_verification(response.json(), valid_user, ["name", "email"])

def test_get_all(client, created_user):
    response = client.get("/users")
    assert_200(response)
    assert_data_verification(response.json()[0], valid_user, ["name", "email"])

def test_get(client, created_user):
    user_id = created_user['id']
    response = client.get(f"/users/{user_id}")
    assert_200(response)
    assert_data_verification(response.json(), {**valid_user, "id": user_id}, ["id","name", "email"])

def test_get_by_email(client, created_user):
    response = client.get(f"/users/by-email?email={valid_user['email']}")
    assert_200(response)
    assert_data_verification(response.json(), {**valid_user, "id": created_user['id']}, ["id","name", "email"])

def test_update_name(client, created_user):
    new_name = {"name": "Updated User"}
    response = client.patch(f"/users/{created_user['id']}", json=new_name)
    assert_200(response)
    assert_data_verification(response.json(), new_name, ["name"])

def test_update_email(client, created_user):
    new_email = {"email": "test2@mail.com"}
    response = client.patch(f"/users/{created_user['id']}", json=new_email)
    assert_200(response)
    assert_data_verification(response.json(), new_email, ["email"])

def test_update_password(client, created_user):
    assert_200(client.patch(f"/users/{created_user['id']}", json={"password": "@123Strong"}))

def test_delete(client, created_user):
    assert_204(client.delete(f"/users/{created_user['id']}"))
    assert_404(client.get(f"/users/{created_user['id']}"))

#Test not found errors
def test_get_all_not_found(client):
    assert_404(client.get("/users"))

def test_get_not_found(client):
    assert_404(client.get(f"/users/1"))

def test_get_by_email_not_found(client):
    assert_404(client.get("/users/by-email?email=test@mail.com"))
 
def test_update_not_found(client):
    assert_404(client.patch(f"/users/1", json={"name": "Updated User"}))

def test_delete_not_found(client):
    assert_404(client.delete(f"/users/1"))


#Test inputs errors
def test_post_duplicate(client, created_user):
    detail_msg = {"detail": "Email already registered"}
    response = client.post("/users", json=valid_user)

    assert_400(response)
    assert_data_verification(response.json(), detail_msg, ["detail"])


def test_update_email_duplicate(client, created_user):
    detail_msg = {"detail": "Email already registered"}
    client.post("/users", json={**valid_user, "email": "test_update@mail.com"})
    response = client.patch(f"/users/{created_user['id']}", json={"email": "test_update@mail.com"})

    assert_400(response)
    assert_data_verification(response.json(), detail_msg, ["detail"])

#Test validation errors
@pytest.mark.parametrize("invalid_user", invalid_user_create_inputs)
def test_post_missing_fields(client, invalid_user):
    assert_422(client.post("/users", json=invalid_user))

@pytest.mark.parametrize("input", invalid_user_passwords)
def test_post_invalid_user_passwords(client, input):
    response = client.post("/users", json={**valid_user, "password": input["password"]})
    assert_422_with_msg(response, input["msg"])

@pytest.mark.parametrize("input", invalid_user_passwords)
def test_update_invalid_user_passwords(client, input):
    user_id = client.post("/users", json=valid_user).json()["id"]
    response = client.patch(f"/users/{user_id}", json={"password": input["password"]})
    assert_422_with_msg(response, input["msg"])