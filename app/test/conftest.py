import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import get_db
from app.db.base import Base
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db

def assert_200(response):  assert response.status_code == 200
def assert_201(response):  assert response.status_code == 201
def assert_204(response):  assert response.status_code == 204
def assert_400(response):  assert response.status_code == 400
def assert_401(response):  assert response.status_code == 401
def assert_404(response):  assert response.status_code == 404
def assert_422(response):  assert response.status_code == 422

def assert_422_with_msg(response, msg: str): 
    assert response.status_code == 422
    assert msg in response.json()["detail"][0]["msg"]

def assert_data_verification(data_get: dict, data_expected: dict, fields: list):
    for field in fields:
        assert field in data_get, f"Missing field '{field}' in response {data_get}"
        assert field in data_expected, f"Missing field '{field}' in expected data {data_expected}"
        assert data_get[field] == data_expected[field], (
            f"Field '{field}' mismatch: expected {data_expected[field]}, got {data_get[field]}"
        )

@pytest.fixture(scope="function")
def client(test_db):
    return TestClient(app)