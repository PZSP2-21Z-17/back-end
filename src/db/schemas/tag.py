from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import  Text, Integer

from src.db.database import BaseModel as BaseSchema

class Tag(BaseSchema):
    __tablename__   = 'tag'
    # Main fields
    tag_code        = Column(Integer, primary_key=True,autoincrement=True, nullable=False)
    name            = Column(Text(20), nullable=False, unique=True)

    # Children
    tag_affs        = relationship("TagAffiliation", back_populates='tags')
