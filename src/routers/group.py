from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.group import Group as GroupModel
from src.schemas.group import *

router = APIRouter()

@router.post("/create/", response_model=GroupSchema)
def create(group: GroupSchema, db: Session = Depends(get_db)):
    db_group = GroupModel(**group.dict())
    try:
        db.add(db_group)
        db.commit()
        db.refresh(db_group)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_group

@router.get("/all/", response_model=List[GroupSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_group = db.query(GroupModel).all()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_group

@router.get("/answers/{exam_id}/{group_nr}", response_model=GroupWithAnswers)
def answers(exam_id: int, group_nr: int, db: Session = Depends(get_db)):
    try:
        db_group = db.query(GroupModel).filter(GroupModel.exam_id == exam_id).filter(GroupModel.group_nr == group_nr).one()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_group
