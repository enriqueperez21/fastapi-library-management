from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.db.session import get_db
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services.user import consult_user_by_email, register_user_service, update_user_service, delete_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=UserOut)
def search_user_by_email_endpoint(email: EmailStr, db: Session = Depends(get_db)):
    return consult_user_by_email(db, email)

@router.post("", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return register_user_service(db, user)

@router.patch("/{user_id}", response_model=UserOut)
def update_user_endpoint(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, updates)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    delete_user_service(db, user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)