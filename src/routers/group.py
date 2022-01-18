from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.group_manager import GroupManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.group import Group
from src.models.group import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=GroupModel)
def create(group: GroupCreate, group_manager: GroupManager = Depends(GroupManager)):
    try:
        return group_manager.add(Group(**group.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[GroupModel])
def all(group_manager: GroupManager = Depends(GroupManager)):
    try:
        a = group_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{exam_id}/{group_nr}", response_model=GroupModel)
def one(exam_id: int, group_nr: int, group_manager: GroupManager = Depends(GroupManager)):
    try:
        a = group_manager.getOne(exam_id, group_nr)
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/answers/{exam_id}/{group_nr}", response_model=GroupWithAnswers)
def answers(exam_id: int, group_nr: int, group_manager: GroupManager = Depends(GroupManager)):
    try:
        a = group_manager.getAnswers(exam_id, group_nr)
        return a
    except ManagerError:
        raise HTTPUnauthorized()
