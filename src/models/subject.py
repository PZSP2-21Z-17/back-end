from pydantic import BaseModel

class SubjectBase(BaseModel):
    subject_code: str

    class Config:
        orm_mode = True

class SubjectModel(SubjectBase):
    name: str

class SubjectCreate(BaseModel):
    subject_code: str
    name: str
