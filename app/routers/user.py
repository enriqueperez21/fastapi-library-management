from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.db.session import get_db
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services import user as user_service
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.consult_all(db)

@router.get("/by-email", response_model=UserOut)
def get_user_by_email(email: EmailStr, db: Session = Depends(get_db)):
    return user_service.consult_by_email(db, email)

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_service.consult_by_id(db, user_id)

@router.post("", response_model=UserOut, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register(db, user)

@router.patch("/{user_id}", response_model=UserOut)
def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update(db, user_id, updates)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete(db, user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)