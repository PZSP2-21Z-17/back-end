from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
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

    def login(self, user: UserLogin, response: Response) :
        try:
            db_user = self.db.query(User).filter(User.password == user.password).filter(User.e_mail == user.e_mail).one()
        except DatabaseError as error:
            raise error
        response.set_cookie('key_id', db_user.user_id, max_age=15*60)
        return db_user

    def lookup(self, user_id: int):
        try:
            db_user = self.db.query(User).filter(User.user_id == user_id).one()
        except Exception as error:
            print(error)
            raise HTTPException(status_code=404)
        return db_user

