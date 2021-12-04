from datetime import datetime
from pydantic import BaseModel as BaseSchema

class ExamBase(BaseSchema):
    exam_id: int

    class Config:
        orm_mode = True

class ExamSchema(ExamBase):
    date_of_exam: datetime
    commentary: str
    subject_code: str
    author_id: int
