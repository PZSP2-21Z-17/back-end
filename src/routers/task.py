from typing import List, Optional
from fastapi import APIRouter, Cookie, Depends, Query
from src.db.managers.task_manager import TaskManager
from src.db.managers.exceptions import ManagerError
from src.db.managers.user_manager import UserManager

from src.db.schemas.task import Task
from src.models.task import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=TaskModel)
def create(
    task: TaskCreate,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    task.author_id = user_id
    try:
        return task_manager.add(Task(**task.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[TaskModel])
def all(
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        a = task_manager.all(user_id)
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{task_id}", response_model=TaskModel)
def one(
    task_id: int,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.byId(user_id, task_id)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/delete/", response_model=None)
def delete(
    task: TaskBase,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.delete(user_id, task)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/update/", response_model=TaskModel)
def update(
    task: TaskModel,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.update(user_id, task)
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/one_with_answers/{task_id}", response_model=TaskWithAnswers)
def one_with_answers(
    task_id: int,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.one_with_answers(user_id, task_id)
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all_with_answers/", response_model=List[TaskWithAnswers])
def all_with_answers(
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.all_with_answers(user_id)
    except ManagerError:
        raise HTTPUnauthorized()

@router.post("/create_with_answers/", response_model=TaskWithAnswers)
def create_with_answers(
    task_with_answers: TaskCreateWithAnswers,
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()

    task_with_answers.author_id = user_id
    try:
        return task_manager.create_with_answers(task_with_answers)
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/find", response_model=List[TaskWithAnswersTagsSubject])
def find(
    tags: List[int] = Query([]),
    search_string: str = Query(None),
    subject_code: str = Query(None),
    offset: int = Query(0),
    task_manager: TaskManager = Depends(TaskManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    try:
        return task_manager.find(user_id, tags, search_string, subject_code, offset)
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/search_tips", response_model=List[SearchTip])
def search_tips(
    search_string: str = Query(None),
    offset: int = Query(0),
    task_manager: TaskManager = Depends(TaskManager)
):
    try:
        return task_manager.search_tips(search_string, offset)
    except ManagerError:
        raise HTTPUnauthorized()