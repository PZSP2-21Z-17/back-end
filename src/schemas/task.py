from datetime import datetime
from pydantic import BaseModel as BaseSchema

class TaskBase(BaseSchema):
    task_id: int

    class Config:
        orm_mode = True

class TaskSchema(BaseSchema):
    contents: str
    score: int
    date_creation: datetime
    is_visible: str
    subject_code: str
    author_id: int
