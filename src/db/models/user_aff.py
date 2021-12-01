from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text, Numeric

from src.db.database import BaseModel

class UserAffiliation(BaseModel):
    __tablename__   = 'user_affiliation'
    # Main fields
    subject_code    = Column(Text(5), ForeignKey('subject.subject_code'), primary_key=True, nullable=False)
    user_id         = Column(Integer, ForeignKey('user.user_id'), primary_key=True, nullable=False)
