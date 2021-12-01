from pydantic import BaseModel as BaseSchema

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

class UserCreate(BaseSchema):
    password: str
    first_name: str
    last_name: str
    e_mail: str
