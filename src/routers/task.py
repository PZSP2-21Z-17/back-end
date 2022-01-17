from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.task import Task
from src.db.schemas.answer import Answer
from src.models.task import *

router = APIRouter()

@router.post("/create/", response_model=TaskModel)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.dict())
    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_task

@router.get("/all/", response_model=List[TaskModel])
def all(db: Session = Depends(get_db)):
    try:
        db_task = db.query(Task).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task

@router.get("/one/{task_id}", response_model=TaskModel)
def one(task_id: int, db: Session = Depends(get_db)):
    try:
        db_task = db.query(Task).filter(Task.task_id == task_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task

@router.post("/delete/", response_model=None)
def delete(task: TaskBase, db: Session = Depends(get_db)):
    try:
        db.query(Task).filter(Task.task_id == task.task_id).delete()
        db.commit()
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return

@router.post("/update/", response_model=TaskModel)
def update(task: TaskModel, db: Session = Depends(get_db)):
    try:
        db.query(Task).filter(Task.task_id == task.task_id).update(task.dict())
        db.commit()
        db_task = db.query(Task).filter(Task.task_id == task.task_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task

@router.get("/one_with_answers/{task_id}", response_model=TaskWithAnswers)
def one_with_answers(task_id: int, db: Session = Depends(get_db)):
    try:
        db_task = db.query(Task).filter(Task.task_id == task_id).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_task

@router.get("/all_with_answers/", response_model=List[TaskWithAnswers])
def all_with_answers(db: Session = Depends(get_db)):
    try:
        db_tasks = db.query(Task).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tasks

@router.post("/create_with_answers/", response_model=TaskWithAnswers)
def create_with_answers(task_with_answers: TaskCreateWithAnswers, db: Session = Depends(get_db)):
    task = TaskCreate(**task_with_answers.dict())
    db_task = Task(**task.dict())
    db_answers = [Answer(**answer.dict()) for answer in task_with_answers.answers]
    try:
        db.add(db_task)
        for db_answer in db_answers:
            db_task.answers.append(db_answer)
        db.commit()
        db.refresh(db_task)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_task
