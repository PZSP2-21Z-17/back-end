from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.subject import Subject as SubjectModel
from src.models.subject import *

router = APIRouter()

@router.post("/create/", response_model=SubjectModel)
def create(subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = SubjectModel(**subject.dict())
    try:
        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_subject

@router.get("/all/", response_model=List[SubjectModel])
def all(db: Session = Depends(get_db)):
    try:
        db_subject = db.query(SubjectModel).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_subject

@router.get("/one/{subject_code}", response_model=SubjectModel)
def one(subject_code: str, db: Session = Depends(get_db)):
    try:
        db_subject = db.query(SubjectModel).filter(SubjectModel.subject_code == subject_code).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_subject
