from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Numeric, Text

from src.db.database import BaseModel

class TaskAffiliation(BaseModel):
    __tablename__   = "task_affiliation"
    # Main fields
    nr_on_sheet     = Column(Integer, nullable=False)
    # Parents
    group_nr        = Column(Integer, ForeignKey('group.group_nr'), primary_key=True, nullable=False)
    exam_id         = Column(Integer, ForeignKey('group.exam_id'), primary_key=True, nullable=False)
    group           = relationship("Group", foreign_keys=[group_nr, exam_id], primaryjoin="and_(Group.group_nr == TaskAffiliation.group_nr, Group.exam_id == TaskAffiliation.exam_id)")
    
    task_id         = Column(Integer, ForeignKey('task.task_id'), primary_key=True, nullable=False)
    task            = relationship("Task")