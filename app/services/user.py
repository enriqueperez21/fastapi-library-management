from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password
from app.models.user import User
from app.crud.user import get_user_by_email, get_user_by_id, create_user, update_user, delete_user

def consult_user_by_email(db: Session, email: str) -> User:
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")
    return user

def register_user_service(db: Session, user: UserCreate) -> User:
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    return create_user(db, user, hashed)

def update_user_service(db: Session, user_id: int, updates: UserUpdate) -> User:
    user = get_user_by_id(db, user_id)
    if not user: raise HTTPException(status_code=404, detail="User not found")

    existing = get_user_by_email(db, updates.email)
    if existing and existing.id != user.id:
        raise HTTPException(status_code=400, detail="Email already registered")

    return update_user(db, user, updates)

def delete_user_service(db: Session, user_id: int) -> None:
    user = get_user_by_id(db, user_id)
    if not user: raise HTTPException(status_code=404, detail="User not found")

    delete_user(db, user)