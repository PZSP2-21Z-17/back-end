from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.user import User
from src.models.user import *

class UserManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def register(self, user: UserCreate):
        db_user = User(**user.dict())
        try:
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return db_user

    def login(self, user: UserLogin):
        try:
            db_user = self.db.query(User).filter(User.password == user.password).filter(User.e_mail == user.e_mail).one()
        except (DatabaseError, NoResultFound) as error:
            raise error
        return db_user

    def lookup(self, user_id: UUID):
        try:
            db_user = self.db.query(User).filter(User.user_id == user_id).one()
        except (DatabaseError, NoResultFound) as error:
            raise error
        return db_user

    def is_user(self, user_id: UUID) -> bool:
        try:
            db_user = self.db.query(User).filter(User.user_id == user_id).one()
        except (DatabaseError, NoResultFound) as error:
            return False
        return True

