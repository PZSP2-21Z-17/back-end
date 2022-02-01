from typing import List
from fastapi import APIRouter, Depends

from src.db.managers.answer_manager import AnswerManager
from src.db.managers.exceptions import ManagerError
from src.db.schemas.answer import Answer
from src.models.answer import AnswerCreate, AnswerModel
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()


@router.post("/create/", response_model=AnswerModel)
def create(answer: AnswerCreate, answer_manager: AnswerManager = Depends(AnswerManager)):
    try:
        return answer_manager.add(Answer(**answer.dict()))
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/all/", response_model=List[AnswerModel])
def all(answer_manager: AnswerManager = Depends(AnswerManager)):
    try:
        a = answer_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()


@router.get("/one/{answer_id}", response_model=AnswerModel)
def one(answer_id: int, answer_manager: AnswerManager = Depends(AnswerManager)):
    try:
        return answer_manager.byId(answer_id)
    except ManagerError:
        raise HTTPUnauthorized()
