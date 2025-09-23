from sqlalchemy import inspect
from app.db.base import Base
from sqlalchemy import text
from app.db.session import engine

def test_connection(client):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1

def test_tables_created(client):
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)

    expected_tables = {"users", "authors", "books"}
    existing_tables = set(inspector.get_table_names())

    for table in expected_tables:
        assert table in existing_tables