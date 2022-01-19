from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import  VARCHAR, Integer

from src.db.database import BaseModel as BaseSchema

class Tag(BaseSchema):
    __tablename__   = 'tag'
    # Main fields
    tag_id          = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name            = Column(VARCHAR(100), nullable=False, unique=True)

    # Children
    tag_affs        = relationship("TagAffiliation", back_populates='tags')
    tasks           = relationship("Task", secondary='tag_affiliation', back_populates='tags', overlaps="tag_affs,tags,tasks")
