from sqlalchemy.orm import Session
from app.models.book import Book
from app.models.author import Author
from app.schemas.book import BookSearch
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

def search_book(db: Session, book_search: BookSearch):
    query = (
        db.query(Book.id, Book.title, Book.year_publication, Author.name.label("author_name"), Book.user_borrow_id)
        .join(Author)
    )

    if book_search.title:
        query = query.filter(Book.title.ilike(f"%{book_search.title}%"))
    if book_search.author_name:
        query = query.filter(Author.name.ilike(f"%{book_search.author_name}%"))
    if book_search.year:
        query = query.filter(Book.year_publication == book_search.year)

    results = query.all()
    return results