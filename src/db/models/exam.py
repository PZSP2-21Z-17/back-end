from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Numeric, Text

from src.db.database import BaseModel

class Exam(BaseModel):
    __tablename__   = 'exam'
    exam_nr         = Column(Numeric(5), primary_key=True, nullable=False)
    subject_code    = Column(Text(5), ForeignKey('subject.subject_code'), primary_key=True, nullable=False)
    user_nr         = Column(Numeric(3), ForeignKey('user.user_nr'), nullable=False)
    date_of_exam    = Column(DateTime, nullable=False)
    commentary      = Column(Text(100))

    # Ongoing relationships from this table to table:
    groups              = relationship("Group")
