from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, example="Clean Code")
    year_publication: Optional[int] = Field(None, ge=0, example=2008)

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BookBase):
    author_id: int = Field(..., example=1)


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, example="Refactoring")
    year_publication: Optional[int] = Field(None, ge=0, example=1999)
    author_id: Optional[int] = Field(None, example=1)

    model_config = ConfigDict(from_attributes=True)


class BookOut(BaseModel):
    id: int
    title: str
    year_publication: Optional[int]
    author_id: int
    user_borrow_id: Optional[int]

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "id": 1,
            "title": "Clean Code",
            "year_publication": 2008,
            "author_id": 1,
            "user_borrow_id": 2
        }
    })