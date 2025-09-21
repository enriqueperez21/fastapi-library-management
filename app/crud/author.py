from sqlalchemy.orm import Session
from app.models.author import Author
from typing import List

def get_authors(db: Session) -> List[Author]:
    return db.query(Author).all()

def get_author_by_id(db: Session, author_id: int) -> Author:
    return db.query(Author).filter(Author.id == author_id).first()

def create_author(db: Session, author: Author) -> Author:
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def update_author(db: Session, author: Author) -> Author:
    db.commit()
    db.refresh(author)
    return author

def delete_author(db: Session, author: Author) -> None:
    db.delete(author)
    db.commit()