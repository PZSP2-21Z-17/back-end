from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.managers.subject_manager import SubjectManager
from src.db.managers.exceptions import ManagerError

from src.dependencies import get_db
from src.db.schemas.subject import Subject
from src.models.subject import *
from src.routers.exceptions import HTTPUnauthorized


router = APIRouter()

@router.post("/create/", response_model=SubjectModel)
def create(subject: SubjectCreate, subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.add(Subject(**subject.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[SubjectModel])
def all(subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        a = subject_manager.all()
        return a
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/one/{subject_code}", response_model=SubjectModel)
def one(subject_code: str, subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.byCode(subject_code)
    except ManagerError:
        raise HTTPUnauthorized()
