from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text

from src.db.database import BaseModel as BaseSchema

class UserAffiliation(BaseSchema):
    __tablename__   = 'user_affiliation'
    # Main fields
    subject_code    = Column(Text(5), ForeignKey('subject.subject_code'), primary_key=True, nullable=False)
    user_id         = Column(Integer, ForeignKey('user.user_id'), primary_key=True, nullable=False)

    # Parents
    subjects        = relationship("Subject", back_populates='user_affs', overlaps="users")
    users           = relationship("User", back_populates='user_affs', overlaps="users")


