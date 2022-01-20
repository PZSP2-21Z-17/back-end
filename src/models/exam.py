from datetime import datetime
from pydantic import BaseModel
from typing import List

class ExamBase(BaseModel):
    exam_id: int

    class Config:
        orm_mode = True

class ExamModel(ExamBase):
    date_of_exam: datetime
    content: str
    description: str
    author_id: str
    description: str

class ExamCreate(BaseModel):
    date_of_exam: datetime
    content: str
    description: str
    author_id: str
    description: str

class ExamGenerate(ExamCreate):
    tasks_per_exam: int
    group_count: int
    task_ids: List[int]
