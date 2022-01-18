from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.exam_manager import ExamManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.exam import Exam
from src.models.exam import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=ExamModel)
def create(answer: ExamCreate, answer_manager: ExamManager = Depends(ExamManager)):
    try:
        return answer_manager.add(Exam(**answer.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[ExamModel])
def all(answer_manager: ExamManager = Depends(ExamManager)):
    try:
        a = answer_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{answer_id}", response_model=ExamModel)
def one(answer_id: int, answer_manager: ExamManager = Depends(ExamManager)):
    try:
        return answer_manager.byId(answer_id)
    except ManagerError:
        raise HTTPUnauthorized()