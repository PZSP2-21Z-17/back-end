from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, VARCHAR

from src.db.database import BaseModel as BaseSchema

class TagAffiliation(BaseSchema):
    __tablename__   = 'tag_affiliation'
    # Main fields
    task_id         = Column(Integer, ForeignKey('task.task_id'), primary_key=True, nullable=False)
    tag_id          = Column(Integer, ForeignKey('tag.tag_id'), primary_key=True, nullable=False)

    # Parent
    tasks           = relationship("Task", back_populates='tag_affs')
    tags            = relationship("Tag", back_populates='tag_affs')