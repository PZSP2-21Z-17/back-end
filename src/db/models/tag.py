from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.sqltypes import  String

from src.db.database import BaseModel

class Tag(BaseModel):
    __tablename__   = 'tag'
    tag_code        = Column(String(5), primary_key=True, nullable=False),
    name            = Column(String(20), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    tag_affiliations    = relationship("TagAffiliation")