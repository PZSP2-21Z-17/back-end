from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.user_aff import UserAffiliation as UserAffiliationModel
from src.schemas.user_aff import *

router = APIRouter()

@router.post("/create/", response_model=UserAffiliationSchema)
def create(user_aff: UserAffiliationCreate, db: Session = Depends(get_db)):
    db_user_aff = UserAffiliationModel(**user_aff.dict())
    try:
        db.add(db_user_aff)
        db.commit()
        db.refresh(db_user_aff)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_user_aff

@router.get("/all/", response_model=List[UserAffiliationSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_user_aff = db.query(UserAffiliationSchema).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_user_aff
