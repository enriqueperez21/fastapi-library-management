import pytest
from app.main import app
from app.core.security import get_current_user
from unittest.mock import patch, MagicMock
from app.models.user import User
from app.test.books.book_data import valid_book
from app.test.users.user_data import valid_user
from app.test.author.author_data import valid_author

@pytest.fixture
def created_author(client): return client.post("/authors", json=valid_author).json()

@pytest.fixture
def created_user(client): return client.post("/users", json=valid_user).json()

@pytest.fixture
def created_book(client, created_author):
    book = {**valid_book, "author_id": created_author["id"]}
    return client.post("/books", json=book).json()

@pytest.fixture
def fake_current_user(created_user):
    def _fake_current_user():
        return User(id=created_user["id"])
    
    app.dependency_overrides[get_current_user] = _fake_current_user
    yield
    app.dependency_overrides.pop(get_current_user, None)

#Test CRUD operations
def test_borrow_book(client, fake_current_user,created_user, created_book):
    response = client.post(f"/books/{created_book['id']}/borrow")
    assert response.status_code == 200
    data = response.json()
    assert data["user_borrow_id"] == created_user["id"]

def test_return_book(client, fake_current_user, created_book):
    client.post(f"/books/{created_book['id']}/borrow")
    response = client.post(f"/books/{created_book['id']}/return")
    assert response.status_code == 200
    data = response.json()
    assert data["user_borrow_id"] == None

#Test invalid scenarios
def test_borrow_nonexistent_book(client, fake_current_user):
    response = client.post("/books/9999/borrow")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

def test_return_nonexistent_book(client, fake_current_user):
    response = client.post("/books/9999/return")
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

def test_borrow_already_borrowed_book(client, fake_current_user, created_book):
    client.post(f"/books/{created_book['id']}/borrow")
    response = client.post(f"/books/{created_book['id']}/borrow")
    assert response.status_code == 400
    assert response.json()["detail"] == "Book is already borrowed"

def test_return_not_borrowed_book(client, fake_current_user, created_book):
    response = client.post(f"/books/{created_book['id']}/return")
    assert response.status_code == 400
    assert response.json()["detail"] == "Book is not borrowed"