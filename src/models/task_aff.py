from pydantic import BaseModel

from .task import TaskWithAnswers


class TaskAffiliationBase(BaseModel):
    group_nr: int
    exam_id: int
    task_id: int

    class Config:
        orm_mode = True


class TaskAffiliationModel(TaskAffiliationBase):
    nr_on_sheet: int


class TaskAffiliationWithAnswers(TaskAffiliationModel):
    tasks: TaskWithAnswers


class TaskAffiliationCreate(BaseModel):
    group_nr: int
    exam_id: int
    task_id: int
    nr_on_sheet: int
