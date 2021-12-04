from pydantic import BaseModel as BaseSchema

class TagAffiliationBase(BaseSchema):
    task_id: int
    tag_code: str

    class Config:
        orm_mode = True

class TagAffiliationSchema(TagAffiliationBase):
    pass
