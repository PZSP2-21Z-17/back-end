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
    except:
        db.rollback()
        return HTTPException()
    return db_answer
