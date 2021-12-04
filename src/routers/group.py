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
    except:
        db.rollback()
        return HTTPException()
    return db_group
