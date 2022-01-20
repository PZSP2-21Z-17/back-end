from typing import List, Optional
from fastapi import APIRouter, Cookie, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.exam_manager import ExamManager
from src.db.managers.exceptions import ManagerError
from src.db.managers.user_manager import UserManager

from src.dependencies import get_db
from src.db.schemas.exam import Exam
from src.models.exam import *
from src.routers.exceptions import HTTPUnauthorized, HTTPBadRequest

router = APIRouter()

@router.post("/create/", response_model=ExamModel)
def create(
    exam: ExamCreate,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    
    exam.author_id = user_id
    try:
        return exam_manager.add(Exam(**exam.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[ExamModel])
def all(
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    
    try:
        a = exam_manager.all(user_id)
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{exam_id}", response_model=ExamModel)
def one(
    exam_id: int,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()
    
    try:
        return exam_manager.byId(user_id, exam_id)
    except ManagerError:
        raise HTTPUnauthorized()


@router.post("/generate/", response_model=ExamModel)
def generate(
    exam_generate: ExamGenerate,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[str] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_manager.lookup(user_id) is None:
        raise HTTPUnauthorized()

    exam_generate.author_id = user_id
    try:
        if exam_generate.tasks_per_exam > len(exam_generate.task_ids):
            raise HTTPBadRequest()
        return exam_manager.generate(exam_generate)
    except ManagerError:
        raise HTTPUnauthorized()