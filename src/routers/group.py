from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Cookie, Depends

from src.db.managers.group_manager import GroupManager
from src.db.managers.exceptions import ManagerError
from src.db.managers.user_manager import UserManager
from src.db.schemas.group import Group
from src.models.group import GroupCreate, GroupModel, GroupWithAnswers
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


@router.get("/{exam_id}/{group_nr}", response_model=GroupWithAnswers)
def one(
    exam_id: int,
    group_nr: int,
    group_manager: GroupManager = Depends(GroupManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()
    try:
        a = group_manager.one(user_id, exam_id, group_nr)
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
