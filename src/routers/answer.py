from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.answer import Answer as AnswerModel
from src.models.answer import *

router = APIRouter()

@router.post("/create/", response_model=AnswerModel)
def create(group: AnswerCreate, db: Session = Depends(get_db)):
    db_answer = AnswerModel(**group.dict())
    try:
        db.add(db_answer)
        db.commit()
        db.refresh(db_answer)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_answer

@router.get("/all/", response_model=List[AnswerModel])
def all(db: Session = Depends(get_db)):
    try:
        db_answer = db.query(AnswerModel).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_answer

@router.get("/one/{answer_id}", response_model=AnswerModel)
def one(answer_id: int, db: Session = Depends(get_db)):
    try:
        db_answer = db.query(AnswerModel).filter(AnswerModel.answer_id == answer_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_answer
