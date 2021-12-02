from pydantic import BaseModel as BaseSchema

class GroupBase(BaseSchema):
    group_nr: int
    exam_id: int

    class Config:
        orm_mode = True
