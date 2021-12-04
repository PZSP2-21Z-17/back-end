from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer

from src.db.database import BaseModel

class Group(BaseModel):
    __tablename__   = 'group'
    # Main fields
    group_nr        = Column(Integer, primary_key=True, nullable=False)

    # Parents
    exam_id         = Column(Integer, ForeignKey('exam.exam_id'), primary_key=True, nullable=False)
    exams           = relationship("Exam", back_populates='groups')

    # Children
    task_affs       = relationship("TaskAffiliation",  primaryjoin="and_(Group.group_nr == TaskAffiliation.group_nr, Group.exam_id == TaskAffiliation.exam_id)", back_populates='groups')
