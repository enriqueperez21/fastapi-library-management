from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import auth as auth_service
from app.schemas.auth import Token, LoginForm, LoginFormDep

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(form_data: LoginForm = Depends(LoginFormDep), db: Session = Depends(get_db)):
    return auth_service.login(db, form_data.email, form_data.password)
