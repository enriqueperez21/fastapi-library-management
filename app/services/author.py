from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorOut, AuthorUpdate
from app.crud import author as author_crud
from typing import List

def get_by_id_with_validation(db: Session, author_id: int) -> AuthorOut:
    author = author_crud.get_author_by_id(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not registered")
    return author

def consult_all(db: Session) -> List[AuthorOut]:
    authors = author_crud.get_authors(db)
    if not authors:
        raise HTTPException(status_code=404, detail="No author has been registered")
    return authors

def consult_by_id(db: Session, author_id: int) -> AuthorOut:
    return get_by_id_with_validation(db, author_id)

def register(db: Session, author: AuthorCreate) -> AuthorOut:
    new_author = Author(
        name=author.name,
        birthdate=author.birthdate
    )
    return author_crud.create_author(db, new_author)

def update(db: Session, author_id: int, updates: AuthorUpdate) -> AuthorOut:
    author = get_by_id_with_validation(db, author_id)
    if updates.name is not None:
        author.name = updates.name
    if updates.birthdate is not None:
        author.birthdate = updates.birthdate

    return author_crud.update_author(db, author)

def delete(db: Session, author_id: int) -> None:
    author = get_by_id_with_validation(db, author_id)

    author_crud.delete_author(db, author)