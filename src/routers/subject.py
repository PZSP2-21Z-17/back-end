from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.subject import Subject as SubjectModel
from src.schemas.subject import *

router = APIRouter()

@router.post("/create/", response_model=SubjectSchema)
def create(subject: SubjectSchema, db: Session = Depends(get_db)):
    db_subject = SubjectModel(**subject.dict())
    try:
        db.add(db_subject)
        db.commit()
        db.refresh(db_subject)
    except:
        db.rollback()
        return HTTPException()
    return db_subject
