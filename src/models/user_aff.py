from pydantic import BaseModel

class UserAffiliationBase(BaseModel):
    subject_code: str
    user_id: int

    class Config:
        orm_mode = True

class UserAffiliationModel(UserAffiliationBase):
    pass

class UserAffiliationCreate(BaseModel):
    subject_code: str
    user_id: int
