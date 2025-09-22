from sqlalchemy.orm import Session
from app.models.book import Book
from typing import List

def get_books(db: Session) -> List[Book]:
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int) -> Book | None:
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def update_book(db: Session, book: Book) -> Book:
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book: Book) -> None:
    db.delete(book)
    db.commit()