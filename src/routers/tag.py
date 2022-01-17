from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.db.schemas.tag import Tag
from src.models.tag import *

router = APIRouter()

@router.post("/create/", response_model=TagModel)
def create(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = Tag(**tag.dict())
    try:
        db.add(db_tag)
        db.commit()
        db.refresh(db_tag)
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return db_tag

@router.get("/all/", response_model=List[TagModel])
def all(db: Session = Depends(get_db)):
    try:
        db_tags = db.query(Tag).all()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tags

@router.get("/one/{tag_code}", response_model=TagModel)
def one(tag_code: str, db: Session = Depends(get_db)):
    try:
        db_tag = db.query(Tag).filter(Tag.tag_code == tag_code).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tag

@router.post("/delete/", response_model=None)
def delete(tag: TagBase, db: Session = Depends(get_db)):
    try:
        db.query(Tag).filter(Tag.tag_code == tag.tag_code).delete()
        db.commit()
    except Exception as error:
        print(error)
        db.rollback()
        raise HTTPException(status_code=404)
    return

@router.post("/update/", response_model=TagModel)
def update(tag: TagModel, db: Session = Depends(get_db)):
    try:
        db.query(Tag).filter(Tag.tag_code == tag.tag_code).update(tag.dict())
        db.commit()
        db_tag = db.query(Tag).filter(Tag.tag_code == tag.tag_code).one()
    except Exception as error:
        print(error)
        raise HTTPException(status_code=404)
    return db_tag
