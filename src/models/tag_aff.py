from pydantic import BaseModel


class TagAffiliationBase(BaseModel):
    task_id: int
    tag_id: int

    class Config:
        orm_mode = True


class TagAffiliationModel(TagAffiliationBase):
    pass


class TagAffiliationCreate(BaseModel):
    task_id: int
    tag_id: int
