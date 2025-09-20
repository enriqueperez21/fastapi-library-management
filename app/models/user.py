from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date, func
from datetime import date
from typing import List

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    registration_date: Mapped[date] = mapped_column(
        Date, server_default=func.current_date(), nullable=False
    )

    books: Mapped[List["Book"]] = relationship(
        back_populates="user_borrow"
    )