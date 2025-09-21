from pydantic import BaseModel, ConfigDict, EmailStr, field_serializer
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)

class UserOut(BaseModel):
    name: str
    email: EmailStr
    registration_date: date

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("registration_date")
    def serialize_date(self, value: date) -> str:
        # 👇 Aquí forzamos formato dd/mm/yyyy
        return value.strftime("%d/%m/%Y")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)