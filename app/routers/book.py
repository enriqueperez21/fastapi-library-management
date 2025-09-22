from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.services import book as book_service
from typing import List

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", response_model=List[BookOut])
def get_books(db: Session = Depends(get_db)):
    return book_service.consult_all(db)

@router.get("/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return book_service.consult_by_id(db, book_id)

@router.post("", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_service.register(db, book)

@router.patch("/{book_id}", response_model=BookOut)
def update_book(book_id: int, updates: BookUpdate, db: Session = Depends(get_db)):
    return book_service.update(db, book_id, updates)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service.delete(db, book_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)