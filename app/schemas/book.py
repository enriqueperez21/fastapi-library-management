from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from fastapi import Query, Depends

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

class BookSearch(BaseModel):
    title: Optional[str] = None
    author_name: Optional[str] = None
    year: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

def BookSearchDep(
    title: Optional[str] = Query(None, example="Clean Code"),
    author_name: Optional[str] = Query(None, example="Robert Martin"),
    year: Optional[int] = Query(None, example=2008),
) -> BookSearch:
    return BookSearch(title=title, author_name=author_name, year=year)

class BookSearchOut(BaseModel):
    id: int
    title: str
    year_publication: Optional[int]
    author_name: str
    user_borrow_id: Optional[int]

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "id": 1,
            "title": "Clean Code",
            "year_publication": 2008,
            "author_name": "Robet Martin",
            "user_borrow_id": 2
        }
    })