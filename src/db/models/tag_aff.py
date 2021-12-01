from sqlalchemy import Column, Integer
from sqlalchemy.orm import relation, relationship, relationships
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Numeric, String

from src.db.database import BaseModel

class TagAffiliation(BaseModel):
    __tablename__   = 'tag_affiliation'
    task_id         = Column(Numeric(5), ForeignKey('task.task_id'), primary_key=True, nullable=False),
    tag_code        = Column(String(5), ForeignKey('tag.tag_code'), primary_key=True, nullable=False)
