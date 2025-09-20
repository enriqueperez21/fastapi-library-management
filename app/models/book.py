from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import Optional

from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year_publication: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    author: Mapped["Author"] = relationship(back_populates="books")

    user_borrow_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    user_borrow: Mapped[Optional["User"]] = relationship(back_populates="books")