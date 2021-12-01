from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Numeric, String

from src.db.database import BaseModel

class TaskAffiliation(BaseModel):
    __tablename__   = "task_affiliation"
    nr_on_sheet     = Column(Numeric(5), nullable=False),
    task_id         = Column(Numeric(5), ForeignKey('task.task_id'), primary_key=True, nullable=False),
    exam_nr         = Column(Numeric(5), ForeignKey('group.exam_nr'), primary_key=True, nullable=False),
    subject_code    = Column(String(5), ForeignKey('group.subject_code'), primary_key=True, nullable=False),
    group_nr        = Column(Numeric(5), ForeignKey('group.group_nr'), primary_key=True, nullable=False),
    user_nr         = Column(Numeric(3), ForeignKey('group.user_nr'), primary_key=True, nullable=False)
