from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.models.tag import Tag as TagModel
from src.dependencies import get_db

from src.schemas.tag import *

router = APIRouter()

@router.post("/create/", response_model=TagSchema)
def create(tag: TagSchema, db: Session = Depends(get_db)):
    db_tag = TagModel(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

@router.get("/all/", response_model=List[TagSchema])
def all(db: Session = Depends(get_db)):
    db_tags = db.query(TagModel).all()
    return db_tags

@router.post("/delete/")
def delete(tag: TagBase, db: Session = Depends(get_db)):
    db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).delete()
    return

@router.get("/one/{tag_code}", response_model=TagSchema)
def one(tag_code: str, db: Session = Depends(get_db)):
    db_tag = db.query(TagModel).filter(TagModel.tag_code == tag_code).one()
    return db_tag

@router.post("/update/", response_model=TagSchema)
def update(tag: TagSchema, db: Session = Depends(get_db)):
    db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).update(tag.dict())
    db.commit()
    db_tag = db.query(TagModel).filter(TagModel.tag_code == tag.tag_code).one()
    return db_tag
