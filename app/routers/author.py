from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.db.session import get_db

router = APIRouter(prefix="/authors", tags=["users"])

@router.get("")
def search_author(name: str, db: Session = Depends(get_db)):
    return {"message": "Author name " + name}