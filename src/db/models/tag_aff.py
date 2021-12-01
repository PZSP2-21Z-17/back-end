from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Numeric, Text

from src.db.database import BaseModel

class TagAffiliation(BaseModel):
    __tablename__   = 'tag_affiliation'
    # Main fields
    task_id         = Column(Integer, ForeignKey('task.task_id'), primary_key=True, nullable=False)
    tag_code        = Column(Text(5), ForeignKey('tag.tag_code'), primary_key=True, nullable=False)
