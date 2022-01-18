from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.exam import Exam
from src.models.exam import *

class ExamManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, exam: Exam) -> Exam:
        try:
            self.db.add(exam)
            self.db.commit()
            self.db.refresh(exam)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return exam

    def all(self) -> List[Exam]:
        try:
            exam = self.db.query(Exam).all()
        except DatabaseError as error:
            raise error
        return exam

    def byId(self, exam_id: int):
        try:
            exam = self.db.query(Exam).filter(Exam.exam_id == exam_id).one()
        except DatabaseError as error:
            raise error
        return exam