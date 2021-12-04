from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.user_aff import UserAffiliation as UserAffiliationModel
from src.schemas.user_aff import *

router = APIRouter()

@router.post("/create/", response_model=UserAffiliationSchema)
def create(user_aff: UserAffiliationSchema, db: Session = Depends(get_db)):
    db_user_aff = UserAffiliationModel(**user_aff.dict())
    try:
        db.add(db_user_aff)
        db.commit()
        db.refresh(db_user_aff)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_user_aff
