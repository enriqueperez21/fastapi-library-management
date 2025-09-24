import pytest
from app.test.conftest import *
from app.test.books.book_data import valid_book, invalid_book_create
from app.test.author.author_data import valid_author
from app.test.users.user_data import valid_user

@pytest.fixture
def created_author(client):
    return client.post("/authors", json=valid_author).json()

@pytest.fixture
def created_user(client):
    return client.post("/users", json=valid_user).json()

@pytest.fixture
def created_book(client, created_author):
    book_data = {**valid_book, "author_id": created_author["id"]}
    return client.post("/books", json=book_data).json()


#Test CRUD operations
def test_post(client, created_author):
    book_data = {**valid_book, "author_id": created_author["id"]}
    response = client.post("/books", json=book_data)
    assert_201(response)
    assert "id" in response.json()
    assert_data_verification(response.json(), book_data, ["title", "year_publication", "author_id"])

def test_get_all(client, created_book):
    response = client.get("/books")
    assert_200(response)
    assert_data_verification(response.json()[0], valid_book, ["title", "year_publication"])

def test_get(client, created_book):
    response = client.get(f"/books/{created_book['id']}")
    assert_200(response)
    assert_data_verification(response.json(), created_book, ["id", "title", "year_publication", "author_id"])

def test_update_title(client, created_book):
    new_title = {"title": "New Title"}
    response = client.patch(f"/books/{created_book['id']}", json=new_title)
    assert_200(response)
    assert_data_verification(response.json(), new_title, ["title"])

def test_update_year(client, created_book):
    new_year = {"year_publication": 2000}
    response = client.patch(f"/books/{created_book['id']}", json=new_year)
    assert_200(response)
    assert_data_verification(response.json(), new_year, ["year_publication"])

def test_update_author(client, created_book):
    author_r = client.post("/authors", json={**valid_author, "name": "New author"})
    new_author_id = {"author_id": author_r.json()["id"]}
    response = client.patch(f"/books/{created_book['id']}", json=new_author_id)
    assert_200(response)
    assert_data_verification(response.json(), new_author_id, ["author_id"])

def test_delete(client, created_book):
    assert_204(client.delete(f"/books/{created_book['id']}"))
    assert_404(client.get(f"/books/{created_book['id']}"))


# Test not found errors
def test_get_all_not_found(client):
    assert_404(client.get("/books"))

def test_get_not_found(client):
    assert_404(client.get(f"/books/1"))

def test_update_not_found(client):
    assert_404(client.patch(f"/books/1", json={"title": "New title"}))

def test_delete_not_found(client):
    assert_404(client.delete(f"/books/1"))


#Test validation errors
def test_post_invalid_author(client):
    response = client.post("/books", json={**valid_book, "author_id": 999})
    assert_404(response)
    assert_data_verification(response.json(), {"detail": "Author not found"}, ["detail"])

def test_post_missing_fields(client, created_author):
    response = client.post("/books", json={**invalid_book_create["input"], "author_id": created_author["id"]})
    assert_422_with_msg(response, invalid_book_create["msg"])

def test_update_invalid_author(client, created_book):
    response = client.patch(f"/books/{created_book['id']}", json={**valid_book, "author_id": 999})
    assert_404(response)
    assert_data_verification(response.json(), {"detail": "Author not found"}, ["detail"])