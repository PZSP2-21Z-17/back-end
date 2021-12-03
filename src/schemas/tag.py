from pydantic import BaseModel as BaseSchema

class TagBase(BaseSchema):
    tag_code: str

    class Config:
        orm_mode = True

class TagSchema(TagBase):
    name: str
