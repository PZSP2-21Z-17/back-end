from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.tag_aff import TagAffiliation as TagAffiliationModel
from src.schemas.tag_aff import *

router = APIRouter()

@router.post("/create/", response_model=TagAffiliationSchema)
def create(tag_aff: TagAffiliationCreate, db: Session = Depends(get_db)):
    db_tag_aff = TagAffiliationModel(**tag_aff.dict())
    try:
        db.add(db_tag_aff)
        db.commit()
        db.refresh(db_tag_aff)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_tag_aff

@router.get("/all/", response_model=List[TagAffiliationSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_tag_aff = db.query(TagAffiliationModel).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tag_aff
