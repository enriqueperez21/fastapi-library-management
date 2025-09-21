# Test Kamina
uvicorn app.main:app --reload
python -m app.db.init_db
python -m pytest -v