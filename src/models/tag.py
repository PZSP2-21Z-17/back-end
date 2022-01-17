from pydantic import BaseModel

class TagBase(BaseModel):
    tag_code: str

    class Config:
        orm_mode = True

class TagModel(TagBase):
    name: str

class TagCreate(BaseModel):
    tag_code: str
    name: str
