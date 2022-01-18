from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.answer import Answer
from src.models.answer import *

class AnswerManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, answer: Answer) -> Answer:
        try:
            self.db.add(answer)
            self.db.commit()
            self.db.refresh(answer)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return answer

    def all(self) -> List[Answer]:
        try:
            answers = self.db.query(Answer).all()
        except DatabaseError as error:
            raise error
        return answers

    def byId(self, answer_id: int):
        try:
            answer = self.db.query(Answer).filter(Answer.answer_id == answer_id).one()
        except DatabaseError as error:
            raise error
        return answer