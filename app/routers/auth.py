from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserOut
from app.services import auth as auth_service
from app.schemas.auth import Token, LoginForm, LoginFormDep

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(form_data: LoginForm = Depends(LoginFormDep), db: Session = Depends(get_db)):
    return auth_service.login(db, form_data.email, form_data.password)

@router.get("/me", response_model=UserOut)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user