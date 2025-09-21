from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorOut

def create_author(db: Session, author: AuthorCreate) -> Author:
    new_author = Author(
        name=author.name,
        birthdate=author.birthdate
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author