from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.answer_manager import AnswerManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.answer import Answer as AnswerModel
from src.models.answer import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=AnswerModel)
def create(group: AnswerCreate, answer_manager: AnswerManager = Depends(AnswerManager)):
    try:
        return answer_manager.add(group)
    except ManagerError:
        raise HTTPUnauthorized()

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
