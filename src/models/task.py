from datetime import datetime
from typing import List
from pydantic import BaseModel

from src.models.subject import SubjectModel
from src.models.tag import TagModel

from .answer import AnswerCreateInTask, AnswerModel

class TaskBase(BaseModel):
    task_id: int

    class Config:
        orm_mode = True

class TaskModel(TaskBase):
    content: str
    date_creation: datetime
    is_visible: str
    subject_code: str

class TaskWithAnswers(TaskModel):
    answers: List[AnswerModel]

class TaskCreate(BaseModel):
    content: str
    date_creation: datetime
    is_visible: str
    subject_code: str
    author_id: str

class TaskCreateWithAnswers(TaskCreate):
    answers: List[AnswerCreateInTask]

class TaskWithAnswersTagsSubject(TaskModel):
    answers: List[AnswerModel]
    tags: List[TagModel]
    subject: SubjectModel

class SearchTip(BaseModel):
    type: str
    id: str
    name: str