from pydantic import BaseModel as BaseSchema

class UserBase(BaseSchema):
    user_id: int

    class Config:
        orm_mode = True

class UserLookup(UserBase):
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
