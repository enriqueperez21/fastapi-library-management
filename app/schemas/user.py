from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer, field_validator
from app.core.types    import PasswordStr
from app.core.validators import validate_secury_password
from typing   import Optional
from datetime import date

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
            "example": {
                "name": "Enrique Pérez",
                "email": "enrique@gmail.com",
                "password": "Contraseña@Segura123"
            }
        })

class UserCreate(UserBase):
    name: str = Field(..., min_length=2, max_length=100, example="Enrique")
    email: EmailStr = Field(..., example="enrique@gmail.com")
    password: PasswordStr = Field(..., example="Strong@Pass123")

    @field_validator("password")
    def validate_password_strength(cls, v: str) -> str:
        return validate_secury_password(v)

class UserUpdate(UserBase):
    name: Optional[str] = Field(None, min_length=2, max_length=100, example="Enrique")
    email: Optional[EmailStr] = Field(None, example="enrique@gmail.com")
    password: Optional[PasswordStr] = Field(None, example="Strong@Pass123")

    @field_validator("password")
    def validate_password_strength(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return validate_secury_password(v)

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    registration_date: date

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "id": 1,
            "name": "Enrique",
            "email": "enrique@gmail.com",
            "registration_date": "21/11/2002"
        }
    })

    @field_serializer("registration_date")
    def serialize_date(self, value: date) -> str:
        return value.strftime("%d/%m/%Y")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True, json_schema_extra={
        "example": {
            "email": "enrique@gmail.com",
            "password": "Strong@Pass123."
        }
    })