from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import  Text

from src.db.database import BaseModel

class Tag(BaseModel):
    __tablename__   = 'tag'
    # Main fields
    tag_code        = Column(Text(5), primary_key=True, nullable=False)
    name            = Column(Text(20), nullable=False, unique=True)

    # Children
    tag_affs        = relationship("TagAffiliation", back_populates='tags')
