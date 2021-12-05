from typing import List
from pydantic import BaseModel as BaseSchema

from .task_aff import TaskAffiliationWithAnswers

class GroupBase(BaseSchema):
    group_nr: int
    exam_id: int

    class Config:
        orm_mode = True

class GroupSchema(GroupBase):
    pass

class GroupWithAnswers(GroupSchema):
    task_affs: List[TaskAffiliationWithAnswers]

class GroupCreate(BaseSchema):
    group_nr: int
    exam_id: int
