from pydantic import BaseModel as BaseSchema

class AnswerBase(BaseSchema):
    answer_id: int

    class Config:
        orm_mode = True

class AnswerSchema(AnswerBase):
    content: str
    is_correct: str
    task_id: int

class AnswerCreate(BaseSchema):
    content: str
    is_correct: str
    task_id: int

class AnswerCreateInTask(BaseSchema):
    content: str
    is_correct: str
