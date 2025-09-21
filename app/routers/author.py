from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.author import AuthorCreate, AuthorOut
from app.services.author import register_author_service

router = APIRouter(prefix="/authors", tags=["authors"])

@router.post("", response_model=AuthorOut)
def search_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return register_author_service(db, author)