from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.answer import Answer as AnswerModel
from src.models.answer import *

class AnswerManager:
    def add(answer: AnswerCreate, db: Session = Depends(get_db)):
        db_answer = AnswerModel(**answer.dict())
        try:
            db.add(db_answer)
            db.commit()
            db.refresh(db_answer)
        except Exception as error:
            print(error)
            db.rollback()
            raise HTTPException(status_code=404)
        return db_answer

    def all():
        pass

    def one():
        pass