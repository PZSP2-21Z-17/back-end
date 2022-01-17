from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.group import Group as GroupModel
from src.models.group import *

router = APIRouter()

@router.post("/create/", response_model=GroupModel)
def create(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = GroupModel(**group.dict())
    try:
        db.add(db_group)
        db.commit()
        db.refresh(db_group)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_group

@router.get("/all/", response_model=List[GroupModel])
def all(db: Session = Depends(get_db)):
    try:
        db_group = db.query(GroupModel).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_group

@router.get("/one/{exam_id}/{group_nr}", response_model=GroupModel)
def one(exam_id: int, group_nr: int, db: Session = Depends(get_db)):
    try:
        db_group = db.query(GroupModel).filter(GroupModel.exam_id == exam_id).filter(GroupModel.group_nr == group_nr).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_group

@router.get("/answers/{exam_id}/{group_nr}", response_model=GroupWithAnswers)
def answers(exam_id: int, group_nr: int, db: Session = Depends(get_db)):
    try:
        db_group = db.query(GroupModel).filter(GroupModel.exam_id == exam_id).filter(GroupModel.group_nr == group_nr).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_group
