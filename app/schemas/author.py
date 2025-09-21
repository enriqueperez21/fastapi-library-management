from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from datetime import date, datetime

class AuthorCreate(BaseModel):
    name: str
    birthdate: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)

    @field_validator("birthdate", mode="before")
    def parse_date(cls, value):
        if value is None:
            return value
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("the date must be in format dd/mm/yyyy (21/11/2002)")
        return value

class AuthorOut(BaseModel):
    id: int
    name: str
    birthdate: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)