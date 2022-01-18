from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.user_aff import UserAffiliation
from src.models.answer import *

class UserAffiliationManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, user_aff: UserAffiliation) -> UserAffiliation:
        try:
            self.db.add(user_aff)
            self.db.commit()
            self.db.refresh(user_aff)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return user_aff

    def all(self) -> List[UserAffiliation]:
        try:
            user_affs = self.db.query(UserAffiliation).all()
        except DatabaseError as error:
            raise error
        return user_affs

