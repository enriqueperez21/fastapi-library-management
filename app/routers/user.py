from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import EmailStr
from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user import register_user, consult_user_by_email

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=UserOut)
def search_user_by_email_endpoint(email: EmailStr, db: Session = Depends(get_db)):
    return consult_user_by_email(db, email)

@router.post("", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)