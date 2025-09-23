from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate, BookSearch, BookSearchOut
from app.crud import book as book_crud, author as author_crud
from app.services import user as user_service
from typing import List

def is_valid_author_id(db: Session, author_id: int) -> None:
    author = author_crud.get_author_by_id(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

def get_by_id_with_validation(db: Session, book_id: int) -> Book:
    book = book_crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def consult_all(db: Session) -> List[Book]:
    books = book_crud.get_books(db)
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    return books

def consult_by_id(db: Session, book_id: int) -> Book:
    return get_by_id_with_validation(db, book_id)

def register(db: Session, book_data: BookCreate) -> Book:
    is_valid_author_id(db, book_data.author_id)
    new_book = Book(
        title=book_data.title,
        year_publication=book_data.year_publication,
        author_id=book_data.author_id
    )
    return book_crud.create_book(db, new_book)

def update(db: Session, book_id: int, updates: BookUpdate) -> Book:
    book = get_by_id_with_validation(db, book_id)

    if updates.title is not None:
        book.title = updates.title
    if updates.year_publication is not None:
        book.year_publication = updates.year_publication
    if updates.author_id is not None:
        is_valid_author_id(db, updates.author_id)
        book.author_id = updates.author_id

    return book_crud.update_book(db, book)

def delete(db: Session, book_id: int) -> None:
    book = get_by_id_with_validation(db, book_id)
    book_crud.delete_book(db, book)

def search(db: Session, book_search: BookSearch) -> List[BookSearchOut]:
    books = book_crud.search_book(db, book_search)
    if not books:
        raise HTTPException(status_code=404, detail="Books searched not founds")
    return books

def borrow(db: Session, book_id: int, user_id: int) -> Book:
    user_service.get_by_id_with_validation(db, user_id)
    book = get_by_id_with_validation(db, book_id)
    if book.user_borrow_id is not None:
        raise HTTPException(status_code=400, detail="Book is already borrowed")
    book.user_borrow_id = user_id
    return book_crud.update_book(db, book)

def return_book(db: Session, book_id: int, user_id: int) -> Book:
    user_service.get_by_id_with_validation(db, user_id)
    book = get_by_id_with_validation(db, book_id)
    if book.user_borrow_id is None:
        raise HTTPException(status_code=400, detail="Book is not borrowed")
    book.user_borrow_id = None
    return book_crud.update_book(db, book)