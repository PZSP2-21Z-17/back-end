from sqlalchemy import Column, Integer

from sqlalchemy.orm import relationship

from ..database import baseModel

class Example(baseModel):
    __tablename__ = 'example_table'

    id = Column(Integer, primary_key=True, index=True)
