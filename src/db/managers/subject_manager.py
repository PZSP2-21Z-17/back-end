from typing import List
from fastapi import Depends
from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.subject import Subject
from src.models.answer import *

class SubjectManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, subject: Subject) -> Subject:
        try:
            self.db.add(subject)
            self.db.commit()
            self.db.refresh(subject)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return subject

    def all(self, offset: int = 0, limit: int = 25):
        try:
            query = self.db.query(Subject.subject_code, Subject.name, Subject.tasks.any().label('in_use')).\
                order_by(Subject.name).\
                limit(limit).\
                offset(limit*offset)
            return query.all()
        except DatabaseError as error:
            raise error
    
    def delete(self, subject_code: str):
        try:
            self.db.query(Subject).\
                filter(Subject.subject_code == subject_code).\
                filter(~Subject.tasks.any()).\
                delete()
            self.db.commit()
            return
        except DatabaseError as error:
            self.db.rollback()
            raise error

    def find(self, search_string: str, offset: int, limit: int = 25) -> List[Subject]:
        try:
            query =  self.db.query(Subject).\
                order_by(desc(func.similarity(Subject.name, search_string))).\
                limit(limit).\
                offset(offset * limit)
            return query.all()
        except DatabaseError as error:
            raise error
