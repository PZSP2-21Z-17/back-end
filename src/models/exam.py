from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from src.models.group import GroupBase


class ExamBase(BaseModel):
    exam_id: int

    class Config:
        orm_mode = True


class ExamModel(ExamBase):
    date_of_exam: datetime
    content: str
    description: str
    author_id: UUID


class ExamCreate(BaseModel):
    date_of_exam: Optional[datetime]
    content: str
    description: str
    author_id: Optional[UUID]


class ExamGenerate(ExamCreate):
    tasks_per_exam: int
    group_count: int
    task_ids: List[int]


class ExamWithGroups(ExamModel):
    groups: List[GroupBase]
