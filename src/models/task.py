from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from src.models.subject import SubjectModel
from src.models.tag import TagBase, TagModel

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
    author_id: Optional[UUID]

class TaskCreateWithTagsAnswers(TaskCreate):
    answers: List[AnswerCreateInTask]
    tags: List[TagBase]

class TaskWithAnswersTagsSubject(TaskModel):
    answers: List[AnswerModel]
    tags: List[TagModel]
    subject: SubjectModel

class TaskWithAnswersTagsSubjectUsage(BaseModel):
    Task: TaskWithAnswersTagsSubject
    in_use: bool

class SearchTip(BaseModel):
    type: str
    id: str
    name: str
