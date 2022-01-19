from pydantic import BaseModel

class TagBase(BaseModel):
    tag_id: int

    class Config:
        orm_mode = True

class TagModel(TagBase):
    name: str

class TagCreate(BaseModel):
    tag_id: int
    name: str