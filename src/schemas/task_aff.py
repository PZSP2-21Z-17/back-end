from typing import List
from pydantic import BaseModel as BaseSchema

from .task import TaskWithAnswers

class TaskAffiliationBase(BaseSchema):
    group_nr: int
    exam_id: int
    task_id: int

    class Config:
        orm_mode = True

class TaskAffiliationSchema(TaskAffiliationBase):
    nr_on_sheet: int

class TaskAffiliationWithAnswers(TaskAffiliationSchema):
    tasks: TaskWithAnswers