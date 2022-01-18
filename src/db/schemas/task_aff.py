from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Integer

from src.db.database import BaseModel as BaseSchema

class TaskAffiliation(BaseSchema):
    __tablename__   = "task_affiliation"
    # Main fields
    nr_on_sheet     = Column(Integer, nullable=False)
    # Parents
    group_nr        = Column(Integer)
    exam_id         = Column(Integer)
    groups          = relationship("Group", foreign_keys=[group_nr, exam_id], primaryjoin="and_(Group.group_nr == TaskAffiliation.group_nr, Group.exam_id == TaskAffiliation.exam_id)", back_populates='task_affs')
    
    task_id         = Column(Integer)
    tasks           = relationship("Task", back_populates='task_affs')

    __table_args__ = (
        ForeignKeyConstraint([group_nr, exam_id], ['group.group_nr', 'group.exam_id']),
        ForeignKeyConstraint([task_id], ['task.task_id']),
        PrimaryKeyConstraint(group_nr, exam_id, task_id),
    {})

    