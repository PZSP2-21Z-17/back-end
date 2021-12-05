from pydantic import BaseModel as BaseSchema

class SubjectBase(BaseSchema):
    subject_code: str

    class Config:
        orm_mode = True

class SubjectSchema(SubjectBase):
    name: str

class SubjectCreate(BaseSchema):
    subject_code: str
    name: str
