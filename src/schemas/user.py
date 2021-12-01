from pydantic import BaseModel as BaseSchema
from fastapi import Form

class BaseUser(BaseSchema):
    user_id: int

    class Config:
        orm_mode = True

class UserLookup(BaseUser):
    first_name: str
    last_name: str
    e_mail: str

class UserLogin(BaseSchema):
    password: str
    e_mail: str

    @classmethod
    def from_form(cls, e_mail: str = Form(...), password: str = Form(...)):
        return cls(e_mail = e_mail, password = password)

class UserCreate(BaseSchema):
    password: str
    first_name: str
    last_name: str
    e_mail: str

    @classmethod
    def from_form(cls, first_name: str = Form(...), last_name: str = Form(...), e_mail: str = Form(...), password: str = Form(...)):
        return cls(first_name = first_name, last_name = last_name, e_mail = e_mail, password = password)