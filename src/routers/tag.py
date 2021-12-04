from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.models.tag import Tag as TagModel
from src.schemas.tag import *

router = APIRouter()

@router.post("/create/", response_model=TagSchema)
def create(tag: TagSchema, db: Session = Depends(get_db)):
    db_tag = TagModel(**tag.dict())
    try:
        db.add(db_tag)
        db.commit()
        db.refresh(db_tag)
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return db_tag

@router.get("/all/", response_model=List[TagSchema])
def all(db: Session = Depends(get_db)):
    try:
        db_tags = db.query(TagModel).all()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_tags

@router.post("/delete/", response_model=None)
def delete(tag: TagBase, db: Session = Depends(get_db)):
    try:
        db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).delete()
        db.commit()
    except Exception as error:
        print(error)
        db.rollback()
        return HTTPException(status_code=404)
    return

@router.get("/one/{tag_code}", response_model=TagSchema)
def one(tag_code: str, db: Session = Depends(get_db)):
    try:
        db_tag = db.query(TagModel).filter(TagModel.tag_code == tag_code).one()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_tag

@router.post("/update/", response_model=TagSchema)
def update(tag: TagSchema, db: Session = Depends(get_db)):
    try:
        db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).update(tag.dict())
        db.commit()
        db_tag = db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).one()
    except Exception as error:
        print(error)
        return HTTPException(status_code=404)
    return db_tag
