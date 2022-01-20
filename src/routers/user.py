from typing import Optional
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from src.db.managers.user_manager import UserManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.user import User
from src.models.user import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

COOKIE_USER_ID = 'user_id'

@router.post("/register/", response_model=UserLookup)
def register(user: UserCreate, user_manager:UserManager = Depends(UserManager)):
    try:
        return user_manager.register(user)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/login/", response_model=bool)
def login(user: UserLogin, response: Response, user_manager: UserManager = Depends(UserManager)):
    try:
        user = user_manager.login(user)
        response.set_cookie(COOKIE_USER_ID, user.user_id, max_age=15*60, secure=True, httponly=True)
        return True
    except ManagerError:
        return False

@router.post("/logout/")
def logout(response: Response):
    response.set_cookie(COOKIE_USER_ID, '', max_age=0, secure=True, httponly=True)
    
@router.get("/is_logged/", response_model=UserLookup)
def is_logged(user_id: Optional[str] = Cookie(None), user_manager: UserManager = Depends(UserManager)):
    if user_id is not None:
        return user_manager.lookup(user_id)
    return HTTPUnauthorized()

@router.get("/lookup/{user_id}", response_model=UserLookup)
def lookup(user_id: int, user_manager:UserManager = Depends(UserManager)):
    try:
        return user_manager.lookup(user_id)
    except ManagerError:
        raise HTTPUnauthorized()
