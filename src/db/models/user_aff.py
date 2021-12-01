from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Text, Numeric

from src.db.database import BaseModel

class UserAffiliation(BaseModel):
    __tablename__   = 'user_affiliation'
    subject_code    = Column(Text(5), ForeignKey('subject.subject_code'), primary_key=True, nullable=False)
    user_nr         = Column(Numeric(3), ForeignKey('user.user_nr'), primary_key=True, nullable=False)

    # Ongoing relationships from this table to table:
    tasks               = relationship("Task")