from typing import List
from fastapi import Depends
from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.tag import Tag 
from src.models.tag import *

class TagManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, tag: Tag) -> Tag:
        try:
            self.db.add(tag)
            self.db.commit()
            self.db.refresh(tag)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return tag

    def all(self, offset: int = 0, limit: int = 25):
        try:
            query = self.db.query(Tag.name, Tag.tag_id, Tag.tag_affs.any().label('in_use')).\
                order_by(Tag.name).\
                limit(limit).\
                offset(offset*limit)
            return query.all()
        except DatabaseError as error:
            raise error
    
    def delete(self, tag: TagBase):
        try:
            query = self.db.query(Tag).filter(Tag.tag_id == tag.tag_id)
            if query.filter(~Tag.tag_affs.any()).first() is not None:
                query.delete()
                self.db.commit()
                return
            else:
                raise DatabaseError()
        except DatabaseError as error:
            raise error

    def find(self, search_string: str, offset: int, limit: int = 25) -> List[Tag]:
        try:
            query =  self.db.query(Tag).\
                order_by(desc(func.similarity(Tag.name, search_string))).\
                limit(limit).\
                offset(offset * limit)
            return query.all()
        except DatabaseError as error:
            raise error
