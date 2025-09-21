from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.author import AuthorCreate, AuthorOut, AuthorUpdate
from app.services import author as author_service
from typing import List

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("", response_model=List[AuthorOut])
def get_authors(db: Session = Depends(get_db)):
    return author_service.consult_all(db)

@router.get("/{author_id}", response_model=AuthorOut)
def get_author(author_id: int, db: Session = Depends(get_db)):
    return author_service.consult_by_id(db, author_id)

@router.post("", response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return author_service.register(db, author)

@router.patch("/{author_id}", response_model=AuthorOut)
def update_author(author_id: int, updates: AuthorUpdate, db: Session = Depends(get_db)):
    return author_service.update(db, author_id, updates)

@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author_service.delete(db, author_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)