from pydantic import BaseModel as BaseSchema

class ExampleCreate(BaseSchema):
    pass

class ExampleLookup(BaseSchema):
    id: int

    class Config:
        orm_mode = True