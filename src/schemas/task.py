from datetime import datetime
from typing import List
from pydantic import BaseModel as BaseSchema

from .answer import AnswerSchema

class TaskBase(BaseSchema):
    task_id: int

    class Config:
        orm_mode = True

class TaskSchema(TaskBase):
    contents: str
    score: int
    date_creation: datetime
    is_visible: str
    subject_code: str
    author_id: int

class TaskWithAnswers(TaskSchema):
    answers: List[AnswerSchema]