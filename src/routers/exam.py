from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.exam import Exam as ExamModel
from src.models.exam import *

router = APIRouter()

@router.post("/create/", response_model=ExamModel)
def create(exam: ExamCreate, db: Session = Depends(get_db)):
    db_exam = ExamModel(**exam.dict())
    try:
        db.add(db_exam)
        db.commit()
        db.refresh(db_exam)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_exam

@router.get("/all/", response_model=List[ExamModel])
def all(db: Session = Depends(get_db)):
    try:
        db_exam = db.query(ExamModel).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_exam

@router.get("/one/{exam_id}", response_model=ExamModel)
def one(exam_id: int, db: Session = Depends(get_db)):
    try:
        db_exam = db.query(ExamModel).filter(ExamModel.exam_id == exam_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_exam
