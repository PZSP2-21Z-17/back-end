from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.user import User as UserModel
from src.models.user import *

router = APIRouter()

@router.post("/register/", response_model=UserLookup)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_user

@router.post("/login/", response_model=UserLookup)
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = db.query(UserModel).filter(UserModel.password == user.password).filter(UserModel.e_mail == user.e_mail).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_user

@router.get("/lookup/{user_id}", response_model=UserLookup)
def lookup(user_id: int, db: Session = Depends(get_db)):
    try:
        db_user = db.query(UserModel).filter(UserModel.user_id == user_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_user
