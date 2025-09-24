import pytest
from app.test.conftest import *
from app.test.author.author_data import valid_author, invalid_author_create_inputs, invalid_author_update_inputs

@pytest.fixture
def created_author(client):
    return client.post("/authors", json=valid_author).json()

#Test CRUD operations
def test_post(client):
    response = client.post("/authors", json=valid_author)
    assert_201(response)
    assert "id" in response.json()
    assert_data_verification(response.json(), valid_author, ["name", "birthdate"])

def test_get_all(client, created_author):
    response = client.get("/authors")
    assert_200(response)
    assert_data_verification(response.json()[0], created_author, ["id","name", "birthdate"])

def test_get(client, created_author):
    response = client.get(f"/authors/{created_author['id']}")
    assert_200(response)
    assert_data_verification(response.json(), created_author, ["id","name", "birthdate"])

def test_update_name(client, created_author):
    new_name = {"name": "Updated Author"}
    response = client.patch(f"/authors/{created_author['id']}", json=new_name)
    assert_200(response)
    assert_data_verification(response.json(), new_name, ["name"])

def test_update_birthdate(client, created_author):
    new_birthdate = {"birthdate": "21/11/2000"}
    response = client.patch(f"/authors/{created_author['id']}", json=new_birthdate)
    assert response.status_code == 200
    assert_data_verification(response.json(), new_birthdate, ["birthdate"])

def test_delete(client, created_author):
    assert_204(client.delete(f"/authors/{created_author['id']}"))
    assert_404(client.get(f"/authors/{created_author['id']}"))

# Test not found errors
def test_get_all_not_found(client):
    assert_404(client.get("/authors"))

def test_get_not_found(client):
    assert_404(client.get(f"/authors/1"))

def test_update_not_found(client):
    assert_404(client.patch(f"/authors/1", json={"name": "Updated Author"}))

def test_delete_not_found(client):
    assert_404(client.delete(f"/authors/1"))

#Test validation errors
@pytest.mark.parametrize("invalid_author", invalid_author_create_inputs)
def test_post_invalid(client, invalid_author):
    response = client.post("/authors", json=invalid_author["input"])
    assert_422_with_msg(response, invalid_author["msg"])

@pytest.mark.parametrize("invalid_author_update", invalid_author_update_inputs)
def test_update_invalid(client, created_author, invalid_author_update):
    response = client.patch(f"/authors/{created_author['id']}", json={"birthdate": invalid_author_update["birthdate"]})
    assert_422_with_msg(response, invalid_author_update["msg"])