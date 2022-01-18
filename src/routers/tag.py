from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.tag_manager import TagManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.tag import Tag
from src.models.tag import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=TagModel)
def create(tag: TagCreate, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.add(Tag(**tag.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[TagModel])
def all( tag_manager: TagManager = Depends(TagManager)):
    try:
        a = tag_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{tag_code}", response_model=TagModel)
def one(tag_code: int, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.byCode(tag_code)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/delete/", response_model=None)
def delete(tag: TagBase,  tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.delete(tag)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/update/", response_model=TagModel)
def update(tag: TagModel, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.update(tag)
    except ManagerError:
        raise HTTPUnauthorized()
