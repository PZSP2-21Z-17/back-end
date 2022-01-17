from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: int

    class Config:
        orm_mode = True

class UserLookup(UserBase):
    first_name: str
    last_name: str
    e_mail: str

class UserLogin(BaseModel):
    password: str
    e_mail: str

class UserCreate(BaseModel):
    password: str
    first_name: str
    last_name: str
    e_mail: str
