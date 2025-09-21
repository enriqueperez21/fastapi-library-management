from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.crud.user import get_user_by_email, create_user
from app.core.security import hash_password

def consult_user_by_email(db: Session, email: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")
    return user

def register_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    return create_user(db, user, hashed)