from http.client import responses
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from src.db.managers.user_manager import UserManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.user import User
from src.models.user import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/register/", response_model=UserLookup)
def register(user: UserCreate, user_manager:UserManager = Depends(UserManager)):
    try:
        return user_manager.register(user)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/login/", response_model=UserLookup)
def login(user: UserLogin, response: Response, user_manager: UserManager = Depends(UserManager)):
    try:
        user = user_manager.login(user)
        response.set_cookie('key_id', str(user.user_id), max_age=15*60)
        return user
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/lookup/{user_id}", response_model=UserLookup)
def lookup(user_id: int, user_manager:UserManager = Depends(UserManager)):
    try:
        return user_manager.lookup(user_id)
    except ManagerError:
        raise HTTPUnauthorized()
