from typing import List
from fastapi import APIRouter, Depends, Query

from src.db.managers.tag_manager import TagManager
from src.db.managers.exceptions import ManagerError
from src.db.schemas.tag import Tag
from src.models.tag import TagBase, TagCreate, TagModel, TagModelWithUsage
from src.routers.exceptions import HTTPForbidden, HTTPUnauthorized

router = APIRouter()


@router.post("/create/", response_model=TagModel)
def create(tag: TagCreate, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.add(Tag(**tag.dict()))
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/all/", response_model=List[TagModelWithUsage])
def all(offset: int = Query(0), tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.all(offset)
    except ManagerError:
        raise HTTPUnauthorized()


@router.delete("/delete/")
def delete(tag: TagBase, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.delete(tag)
    except ManagerError:
        raise HTTPForbidden()


@router.get("/find/", response_model=List[TagModel])
def find(search_string: str, offset: int = 0, tag_manager: TagManager = Depends(TagManager)):
    try:
        return tag_manager.find(search_string, offset)
    except ManagerError:
        raise HTTPUnauthorized()
