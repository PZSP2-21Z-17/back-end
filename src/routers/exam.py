from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.exam import Exam as ExamModel
from src.schemas.exam import *

router = APIRouter()

@router.post("/create/", response_model=ExamSchema)
def create(exam: ExamSchema, db: Session = Depends(get_db)):
    db_exam = ExamModel(**exam.dict())
    try:
        db.add(db_exam)
        db.commit()
        db.refresh(db_exam)
    except:
        db.rollback()
        return HTTPException()
    return db_exam
