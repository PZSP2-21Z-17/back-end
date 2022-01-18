from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.task_aff import TaskAffiliation
from src.models.answer import *

class TaskAffiliationManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, task_aff: TaskAffiliation) -> TaskAffiliation:
        try:
            self.db.add(task_aff)
            self.db.commit()
            self.db.refresh(task_aff)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return task_aff

    def all(self) -> List[TaskAffiliation]:
        try:
            task_affs = self.db.query(TaskAffiliation).all()
        except DatabaseError as error:
            raise error
        return task_affs

    def byId(self, group_nr: int, exam_id: int, task_id: int):
        try:
            task_aff = self.db.query(TaskAffiliation).filter(TaskAffiliation.group_nr == group_nr).filter(TaskAffiliation.exam_id == exam_id).filter(TaskAffiliation.task_id == task_id).one()
        except DatabaseError as error:
            raise error
        return task_aff


