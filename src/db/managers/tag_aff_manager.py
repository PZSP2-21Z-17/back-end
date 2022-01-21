from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.tag_aff import TagAffiliation
from src.models.answer import *
from src.models.tag_aff import TagAffiliationBase

class TagAffiliationManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, tag_aff: TagAffiliation) -> TagAffiliation:
        try:
            self.db.add(tag_aff)
            self.db.commit()
            self.db.refresh(tag_aff)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return tag_aff

    def delete(self, tag_aff: TagAffiliationBase):
        try:
            self.db.query(TagAffiliation).\
                filter(TagAffiliation.tag_id == tag_aff.tag_id).\
                filter(TagAffiliation.task_id == tag_aff.task_id).\
                delete()
        except DatabaseError as error:
            raise error