from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: str

    class Config:
        orm_mode = True

class UserLookup(BaseModel):
    first_name: str
    last_name: str
    e_mail: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    password: str
    e_mail: str

class UserCreate(BaseModel):
    password: str
    first_name: str
    last_name: str
    e_mail: str
