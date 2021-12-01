from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.models import user
from src.dependencies import get_db

from src.schemas import user

router = APIRouter()

@router.get("/create/", response_model=user.UserLookup)
def create(user: user.UserCreate = Depends(user.UserCreate.from_form), db: Session = Depends(get_db)):
    db_user = user.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/lookup/{nr_user}", response_model=user.UserLookup)
def lookup(nr_user: int, db: Session = Depends(get_db)):
    db_user = db.query(user.User).filter(user.User.nr_user == nr_user).one()
    return db_user