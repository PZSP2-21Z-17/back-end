from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.answer import Answer as AnswerModel
from src.schemas.answer import *

router = APIRouter()

@router.post("/create/", response_model=AnswerSchema)
def create(group: AnswerSchema, db: Session = Depends(get_db)):
    db_answer = AnswerModel(**group.dict())
    try:
        db.add(db_answer)
        db.commit()
        db.refresh(db_answer)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_answer

@router.get("/all/", response_model=List[AnswerSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_answer = db.query(AnswerModel).all()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_answer
