from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.task_aff_manager import TaskAffiliationManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.task_aff import TaskAffiliation
from src.models.task_aff import *
from src.routers.exceptions import HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=TaskAffiliationModel)
def create(task_aff: TaskAffiliationCreate,task_aff_manager: TaskAffiliationManager = Depends(TaskAffiliationManager)):
    try:
        return task_aff_manager.add(TaskAffiliation(**task_aff.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[TaskAffiliationModel])
def all(task_aff_manager: TaskAffiliationManager = Depends(TaskAffiliationManager)):
    try:
        a = task_aff_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{group_nr}/{exam_id}/{task_id}", response_model=TaskAffiliationModel)
def one(group_nr: int, exam_id: int, task_id: int, task_aff_manager:TaskAffiliationManager = Depends(TaskAffiliationManager)):
    try:
        return task_aff_manager.byId(group_nr, exam_id, task_id)
    except ManagerError:
        raise HTTPUnauthorized()
