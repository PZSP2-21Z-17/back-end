from typing import Optional
from fastapi import APIRouter, Cookie, Depends, Response

from src.db.managers.user_manager import UserManager
from src.db.managers.exceptions import ManagerError
from src.models.user import UserCreate, UserLogin, UserLookup
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

COOKIE_USER_ID = 'user_id'
CLIENT_SESSION = 10 * 60 * 60


@router.post("/register/", response_model=UserLookup)
def register(user: UserCreate, user_manager: UserManager = Depends(UserManager)):
    try:
        return user_manager.register(user)
    except ManagerError:
        raise HTTPUnauthorized()


@router.post("/login/")
def login(user: UserLogin, response: Response, user_manager: UserManager = Depends(UserManager)):
    try:
        user = user_manager.login(user)
        response.set_cookie(COOKIE_USER_ID, user.user_id, max_age=CLIENT_SESSION, secure=True, httponly=True, samesite="none")
        return
    except ManagerError:
        raise HTTPUnauthorized()


@router.post("/logout/")
def logout(response: Response):
    response.set_cookie(COOKIE_USER_ID, '', max_age=0, secure=True, httponly=True, samesite="none")


@router.get("/is_logged/", response_model=UserLookup)
def is_logged(response: Response, user_id: Optional[str] = Cookie(None), user_manager: UserManager = Depends(UserManager)):
    try:
        if user_id is not None:
            response.set_cookie(COOKIE_USER_ID, user_id, max_age=CLIENT_SESSION, secure=True, httponly=True, samesite="none")
            return user_manager.lookup(user_id)
        else:
            raise HTTPUnauthorized()
    except ManagerError:
        raise HTTPUnauthorized()
