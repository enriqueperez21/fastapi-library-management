from pydantic import BaseModel, ConfigDict, field_validator, field_serializer
from typing import Optional
from datetime import date, datetime

class AuthorBase(BaseModel):
    name: Optional[str] = None
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
    
    @field_serializer("birthdate")
    def serialize_date(self, value: date) -> str:
        # 👇 Aquí forzamos formato dd/mm/yyyy
        return value.strftime("%d/%m/%Y")

class AuthorCreate(AuthorBase):
    name: str

class AuthorUpdate(AuthorBase):
    pass

class AuthorOut(AuthorBase):
    id: int
    name: str