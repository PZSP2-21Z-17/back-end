from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.task_aff import TaskAffiliation as TaskAffiliationModel
from src.schemas.task_aff import *

router = APIRouter()

@router.post("/create/", response_model=TaskAffiliationSchema)
def create(task_aff: TaskAffiliationSchema, db: Session = Depends(get_db)):
    db_task_aff = TaskAffiliationModel(**task_aff.dict())
    try:
        db.add(db_task_aff)
        db.commit()
        db.refresh(db_task_aff)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_task_aff

@router.get("/all/", response_model=List[TaskAffiliationSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_task_aff = db.query(TaskAffiliationSchema).all()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_task_aff
