from sqlalchemy import Column, Integer

from src.db.database import BaseModel

class Example(BaseModel):
    __tablename__ = 'example_table'

    id = Column(Integer, primary_key=True, index=True)
