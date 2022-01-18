from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.group import Group
from src.models.answer import *

class GroupManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, group: Group) -> Group:
        try:
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return group

    def all(self) -> List[Group]:
        try:
            groups = self.db.query(Group).all()
        except DatabaseError as error:
            raise error
        return groups

    def getOne(self, exam_id: int, group_nr:int):
        try:
            groups = self.db.query(Group).filter(Group.exam_id == exam_id).filter(Group.group_nr == group_nr).one()
        except DatabaseError as error:
            raise error
        return groups

    def getAnswers(self,  exam_id: int, group_nr:int):
        try:
            groups = self.db.query(Group).filter(Group.exam_id == exam_id).filter(Group.group_nr == group_nr).one()
        except DatabaseError as error:
            raise error
        return groups


