from datetime import datetime
from typing import List
from pydantic import BaseModel

from .answer import AnswerCreateInTask, AnswerModel

class TaskBase(BaseModel):
    task_id: int

    class Config:
        orm_mode = True

class TaskModel(TaskBase):
    contents: str
    score: int
    date_creation: datetime
    is_visible: str
    subject_code: str
    author_id: int

class TaskWithAnswers(TaskModel):
    answers: List[AnswerModel]

class TaskCreate(BaseModel):
    contents: str
    score: int
    date_creation: datetime
    is_visible: str
    subject_code: str
    author_id: int

class TaskCreateWithAnswers(TaskCreate):
    answers: List[AnswerCreateInTask]