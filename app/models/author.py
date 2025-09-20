from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date
from typing import List, Optional
from datetime import date

from app.db.base import Base

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    birthdate: Mapped[Optional[date]] = mapped_column(
        Date, nullable=True
    )

    books: Mapped[List["Book"]] = relationship(
        back_populates="author"
    )