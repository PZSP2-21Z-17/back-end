from datetime import datetime
from pydantic import BaseModel

class ExamBase(BaseModel):
    exam_id: int

    class Config:
        orm_mode = True

class ExamModel(ExamBase):
    date_of_exam: datetime
    commentary: str
    description: str
    author_id: int

class ExamCreate(BaseModel):
    date_of_exam: datetime
    commentary: str
    description: str
    author_id: int
