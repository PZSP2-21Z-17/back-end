from pydantic import BaseModel as BaseSchema

class UserAffiliationBase(BaseSchema):
    subject_code: str
    user_id: int

    class Config:
        orm_mode = True

class UserAffiliationSchema(UserAffiliationBase):
    pass
