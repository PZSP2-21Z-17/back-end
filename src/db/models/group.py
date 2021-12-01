from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Numeric, Text

from src.db.database import BaseModel
from src.db.models import exam

class Group(BaseModel):
    __tablename__   = 'group'
    # Main fields
    group_nr        = Column(Integer, primary_key=True, nullable=False)
    # Parents
    exam_id         = Column(Integer, ForeignKey('exam.exam_id'), primary_key=True, nullable=False)
    exam            = relationship("Exam")
