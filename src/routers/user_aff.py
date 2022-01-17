from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.user_aff import UserAffiliation
from src.models.user_aff import *

router = APIRouter()

@router.post("/create/", response_model=UserAffiliationModel)
def create(user_aff: UserAffiliationCreate, db: Session = Depends(get_db)):
    db_user_aff = UserAffiliation(**user_aff.dict())
    try:
        db.add(db_user_aff)
        db.commit()
        db.refresh(db_user_aff)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_user_aff

@router.get("/all/", response_model=List[UserAffiliationModel])
def all(db: Session = Depends(get_db)):
    try:
        db_user_aff = db.query(UserAffiliation).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_user_aff
