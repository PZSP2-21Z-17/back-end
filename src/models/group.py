from typing import List
from pydantic import BaseModel

from .task_aff import TaskAffiliationWithAnswers

class GroupBase(BaseModel):
    group_nr: int
    exam_id: int

    class Config:
        orm_mode = True

class GroupModel(GroupBase):
    pass

class GroupWithAnswers(GroupModel):
    task_affs: List[TaskAffiliationWithAnswers]

class GroupCreate(BaseModel):
    group_nr: int
    exam_id: int
