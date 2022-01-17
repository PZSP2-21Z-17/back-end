from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.tag_aff import TagAffiliation
from src.models.tag_aff import *

router = APIRouter()

@router.post("/create/", response_model=TagAffiliationModel)
def create(tag_aff: TagAffiliationCreate, db: Session = Depends(get_db)):
    db_tag_aff = TagAffiliation(**tag_aff.dict())
    try:
        db.add(db_tag_aff)
        db.commit()
        db.refresh(db_tag_aff)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_tag_aff

@router.get("/all/", response_model=List[TagAffiliationModel])
def all(db: Session = Depends(get_db)):
    try:
        db_tag_aff = db.query(TagAffiliation).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tag_aff
