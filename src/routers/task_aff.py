from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.task_aff import TaskAffiliation as TaskAffiliationModel
from src.schemas.task_aff import *

router = APIRouter()

@router.post("/create/", response_model=TaskAffiliationSchema)
def create(task_aff: TaskAffiliationCreate, db: Session = Depends(get_db)):
    db_task_aff = TaskAffiliationModel(**task_aff.dict())
    try:
        db.add(db_task_aff)
        db.commit()
        db.refresh(db_task_aff)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_task_aff

@router.get("/all/", response_model=List[TaskAffiliationSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_task_aff = db.query(TaskAffiliationSchema).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task_aff

@router.get("/one/{group_nr}/{exam_id}/{task_id}", response_model=TaskAffiliationSchema)
def one(group_nr: int, exam_id: int, task_id: int, db: Session = Depends(get_db)):
    try:
        db_task_aff = db.query(TaskAffiliationModel).filter(TaskAffiliationModel.group_nr == group_nr).filter(TaskAffiliationModel.exam_id == exam_id).filter(TaskAffiliationModel.task_id == task_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task_aff
