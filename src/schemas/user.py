from pydantic import BaseModel as BaseSchema
from fastapi import Form

class BaseUser(BaseSchema):
    nr_user: int

    class Config:
        orm_mode = True

class UserLookup(BaseUser):
    first_name: str
    last_name: str
    e_mail: str

class UserCreate(BaseSchema):
    password: str
    first_name: str
    last_name: str
    e_mail: str

    @classmethod
    def from_form(cls, first_name: str = Form(...), last_name: str = Form(...), e_mail: str = Form(...), password: str = Form(...)):
        return cls(first_name, last_name, e_mail, password)