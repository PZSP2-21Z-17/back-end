from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.tag_aff import TagAffiliation
from src.models.answer import *

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

    def all(self) -> List[TagAffiliation]:
        try:
            tag_affs = self.db.query(TagAffiliation).all()
        except DatabaseError as error:
            raise error
        return tag_affs

