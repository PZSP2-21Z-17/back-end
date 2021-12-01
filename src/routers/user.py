from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.models.user import User as UserModel
from src.dependencies import get_db

from src.schemas.user import *

router = APIRouter()

@router.post("/register/", response_model=UserLookup)
def register(user: UserCreate = Depends(UserCreate.from_form), db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/", response_model=UserLookup)
def login(user: UserLogin = Depends(UserLogin.from_form), db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.password == user.password).filter(UserModel.e_mail == user.e_mail).one()
    return db_user

@router.get("/lookup/{user_id}", response_model=UserLookup)
def lookup(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.user_id == user_id).one()
    return db_user