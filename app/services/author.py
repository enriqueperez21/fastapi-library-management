from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorOut
from app.crud.author import create_author

def register_author_service(db: Session, author: AuthorCreate) -> Author:
    return create_author(db, author)