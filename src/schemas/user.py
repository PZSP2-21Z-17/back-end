from pydantic import BaseModel as BaseSchema
from sqlalchemy.sql.sqltypes import String
from fastapi import Form

class BaseUser(BaseSchema):
    nr_user: int

    class Config:
        orm_mode = True

class UserLookup(BaseUser):
    first_name: String
    last_name: String
    e_mail: String

class UserCreate(BaseSchema):
    password: String
    first_name: String
    last_name: String
    e_mail: String

    @classmethod
    def from_form(cls, first_name: str = Form(...), last_name: str = Form(...), e_mail: str = Form(...), password: str = Form(...)):
        return cls(first_name, last_name, e_mail, password)