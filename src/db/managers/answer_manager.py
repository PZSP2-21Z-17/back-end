from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.answer import Answer
from src.models.answer import *

class AnswerManager:
    def add(answer: AnswerCreate, db: Session = Depends(get_db)) -> Answer:
        db_answer = Answer(**answer.dict())
        try:
            db.add(db_answer)
            db.commit()
            db.refresh(db_answer)
        except DatabaseError as error:
            print(error)
            db.rollback()
            raise error
        return db_answer

    def all():
        pass

    def one():
        pass