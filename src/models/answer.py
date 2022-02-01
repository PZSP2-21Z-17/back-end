from pydantic import BaseModel


class AnswerBase(BaseModel):
    answer_id: int

    class Config:
        orm_mode = True


class AnswerModel(AnswerBase):
    content: str
    is_correct: str
    task_id: int


class AnswerCreate(BaseModel):
    content: str
    is_correct: str
    task_id: int


class AnswerCreateInTask(BaseModel):
    content: str
    is_correct: str
