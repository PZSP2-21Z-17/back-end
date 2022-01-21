from typing import List
from fastapi import APIRouter, Depends, Query
from src.db.managers.subject_manager import SubjectManager
from src.db.managers.exceptions import ManagerError

from src.db.schemas.subject import Subject
from src.models.subject import *
from src.routers.exceptions import HTTPForbidden, HTTPUnauthorized

router = APIRouter()

@router.post("/create/", response_model=SubjectModel)
def create(subject: SubjectCreate, subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.add(Subject(**subject.dict()))
    except ManagerError:
        raise HTTPUnauthorized()

@router.get("/all/", response_model=List[SubjectModelWithUsage])
def all(offset: int = Query(0), subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.all(offset)
    except ManagerError:
        raise HTTPUnauthorized()

@router.delete("/delete/")
def delete(subject: SubjectBase, subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.delete(subject)
    except ManagerError:
        raise HTTPForbidden()

@router.get("/find/", response_model=List[SubjectModel])
def find(search_string: str, offset: int = 0, subject_manager: SubjectManager = Depends(SubjectManager)):
    try:
        return subject_manager.find(search_string, offset)
    except ManagerError:
        raise HTTPUnauthorized()
