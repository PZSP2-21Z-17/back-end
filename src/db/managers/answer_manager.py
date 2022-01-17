from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.answer import Answer
from src.models.answer import *

class AnswerManager:
    def add(answer: Answer, db: Session = Depends(get_db)) -> Answer:
        try:
            db.add(answer)
            db.commit()
            db.refresh(answer)
        except DatabaseError as error:
            db.rollback()
            raise error
        return answer

    def all(db: Session = Depends(get_db)) -> List[Answer]:
        try:
            answers = db.query(AnswerModel).all()
        except DatabaseError as error:
            raise error
        return answers

    def byId(answer_id: int, db: Session = Depends(get_db)):
        try:
            answer = db.query(Answer).filter(Answer.answer_id == answer_id).one()
        except DatabaseError as error:
            raise error
        return answer