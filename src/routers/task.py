from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.task import Task as TaskModel
from src.schemas.task import *

router = APIRouter()

@router.post("/create/", response_model=TaskSchema)
def create(task: TaskSchema, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.dict())
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_task

@router.get("/all/", response_model=List[TaskSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_task = db.query(TaskSchema).all()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_task
