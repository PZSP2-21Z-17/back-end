from typing import List
from fastapi import Depends
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

    def all(self) -> List[Tag]:
        try:
            tags = self.db.query(Tag).all()
        except DatabaseError as error:
            raise error
        return tags

    def byCode(self, tag_code: int):
        try:
            tag = self.db.query(Tag).filter(Tag.tag_code == tag_code).one()
        except DatabaseError as error:
            raise error
        return tag


    def delete(self, tag: TagBase):
        try:
            self.db.query(Tag).filter(Tag.tag_code == tag.tag_code).delete()
            self.db.commit()
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return 


    def update(self, tag: TagModel):
        try:
            self.db.query(Tag).filter(Tag.tag_code == tag.tag_code).update(tag.dict())
            self.db.commit()
            db_tag = self.db.query(Tag).filter(Tag.tag_code == tag.tag_code).one()        
        except DatabaseError as error:
            raise error
        return db_tag

