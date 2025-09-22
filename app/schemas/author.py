from pydantic import BaseModel, ConfigDict, Field, field_validator, field_serializer
from typing import Optional
from datetime import date, datetime

class AuthorBase(BaseModel):
    name: Optional[str] = Field(
        None, 
        example="Robert Martin"
    )
    birthdate: Optional[date] = Field(
        None, 
        example="21/11/2002",
        description="Date of birth in format dd/mm/yyyy"
    )

    model_config = ConfigDict(from_attributes=True)

    @field_validator("birthdate", mode="before")
    def parse_date(cls, value):
        if value is None:
            return value
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("The date must be in format dd/mm/yyyy (21/11/2002)")
        return value
    
    @field_serializer("birthdate")
    def serialize_date(self, value: date) -> str:
        return value.strftime("%d/%m/%Y")

class AuthorCreate(AuthorBase):
    name: str = Field(
        None, 
        example="Robert Martin"
    )

class AuthorUpdate(AuthorBase):
    pass

class AuthorOut(AuthorBase):
    id: int
    name: str = Field(
        None, 
        example="Enrique Pérez"
    )