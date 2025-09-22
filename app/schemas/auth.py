from pydantic import BaseModel, EmailStr, Field
from fastapi import Form

class LoginForm(BaseModel):
    email: EmailStr
    password: str

def LoginFormDep(
    email: EmailStr = Form(...),
    password: str = Form(...)
) -> LoginForm:
    return LoginForm(email=email, password=password)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: int
    email: str