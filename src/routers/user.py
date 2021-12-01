from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.models import user as user_model
from src.dependencies import get_db

from src.schemas import user as user_schema

router = APIRouter()

@router.post("/create/", response_model=user_schema.UserLookup)
def create(user: user_schema.UserCreate = Depends(user_schema.UserCreate.from_form), db: Session = Depends(get_db)):
    db_user = user_model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/lookup/{user_id}", response_model=user_schema.UserLookup)
def lookup(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.user_id == user_id).one()
    return db_user