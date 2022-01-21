from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.tag_aff_manager import TagAffiliationManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.tag_aff import TagAffiliation
from src.models.tag_aff import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=TagAffiliationModel)
def create(tag_aff: TagAffiliationCreate, tag_aff_manager: TagAffiliationManager= Depends(TagAffiliationManager)):
    try:
        return tag_aff_manager.add(TagAffiliation(**tag_aff.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.delete("/delete/")
def create(tag_aff: TagAffiliationBase, tag_aff_manager: TagAffiliationManager= Depends(TagAffiliationManager)):
    try:
        return tag_aff_manager.delete(tag_aff)
    except ManagerError:
        raise HTTPUnauthorized()
