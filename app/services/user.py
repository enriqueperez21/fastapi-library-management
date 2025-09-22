from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.core.security import hash_password
from app.crud import user as user_crud
from typing import List

def get_by_id_with_validation(db: Session, user_id: int) -> UserOut:
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not registered")
    return user

def consult_by_email(db: Session, email: str) -> UserOut:
    user = user_crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Email not registered")
    return user

def consult_by_id(db: Session, user_id: int) -> UserOut:
    return get_by_id_with_validation(db, user_id)

def consult_all(db: Session) -> List[UserOut]:
    users = user_crud.get_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

def register(db: Session, user: UserCreate) -> UserOut:
    if user_crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    return user_crud.create_user(db, new_user)

def update(db: Session, user_id: int, updates: UserUpdate) -> UserOut:
    user = get_by_id_with_validation(db, user_id)

    if updates.email is not None:
        existing = user_crud.get_user_by_email(db, updates.email)
        if existing and existing.id != user.id:
            raise HTTPException(status_code=400, detail="Email already registered")
        user.email = updates.email

    if updates.name is not None:
        user.name = updates.name

    if updates.password is not None:
        user.password = hash_password(updates.password)

    return user_crud.update_user(db, user)

def delete(db: Session, user_id: int) -> None:
    user = get_by_id_with_validation(db, user_id)
    user_crud.delete_user(db, user)