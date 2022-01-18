from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.user_aff_manager import UserAffiliationManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.user_aff import UserAffiliation
from src.models.user_aff import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=UserAffiliationModel)
def create(user_aff: UserAffiliationCreate, user_aff_manager: UserAffiliationManager = Depends(UserAffiliationManager)):
    try:
        return user_aff_manager.add(UserAffiliation(**user_aff.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[UserAffiliationModel])
def all(user_aff_manager: UserAffiliationManager = Depends(UserAffiliationManager)):
    try:
        a = user_aff_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()
