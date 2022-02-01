from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, Cookie, Depends
from typing import List, Optional

from src.db.managers.exam_manager import ExamManager
from src.db.managers.exceptions import ManagerError
from src.db.managers.user_manager import UserManager
from src.db.schemas.exam import Exam
from src.models.exam import ExamBase, ExamCreate, ExamGenerate, ExamModel, ExamWithGroups
from src.routers.exceptions import HTTPUnauthorized, HTTPBadRequest

router = APIRouter()


@router.post("/create/", response_model=ExamModel)
def create(
    exam: ExamCreate,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()

    exam.author_id = user_id
    try:
        return exam_manager.add(Exam(**exam.dict()))
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/all/", response_model=List[ExamWithGroups])
def all(
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()

    try:
        a = exam_manager.all(user_id)
        return a
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/{exam_id}/groups/", response_model=ExamWithGroups)
def groups(
    exam_id: int,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()

    try:
        return exam_manager.groups(user_id, exam_id)
    except ManagerError:
        raise HTTPUnauthorized()


@router.post("/delete/", response_model=None)
def delete(
    exam: ExamBase,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()
    try:
        return exam_manager.delete(user_id, exam)
    except ManagerError:
        raise HTTPUnauthorized()


@router.post("/generate/", response_model=ExamModel)
def generate(
    exam_generate: ExamGenerate,
    exam_manager: ExamManager = Depends(ExamManager),
    user_id: Optional[UUID] = Cookie(None),
    user_manager: UserManager = Depends(UserManager)
):
    if user_id is None or not user_manager.is_user(user_id):
        raise HTTPUnauthorized()

    exam_generate.author_id = user_id
    exam_generate.date_of_exam = datetime.utcnow()
    try:
        if exam_generate.tasks_per_exam > len(exam_generate.task_ids):
            raise HTTPBadRequest()
        return exam_manager.generate(exam_generate)
    except ManagerError:
        raise HTTPUnauthorized()
