from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.models import example
from src.dependencies import get_db

router = APIRouter()

@router.get("/")
def index(db: Session = Depends(get_db)):
    return db.query(example.Example).all()