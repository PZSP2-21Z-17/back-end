from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Numeric, Text

from src.db.database import BaseModel

class Group(BaseModel):
    __tablename__   = 'group'
    group_nr        = Column(Numeric(5), primary_key=True, nullable=False)
    exam_nr         = Column(Numeric(5), ForeignKey('exam.exam_nr'), primary_key=True, nullable=False)
    subject_code    = Column(Text(5), ForeignKey('exam.subject_code'), primary_key=True, nullable=False)
    user_nr         = Column(Numeric(3), ForeignKey('exam.user_nr'), primary_key=True, nullable=False)

    # Ongoing relationships from this table to table:
    task_affiliations   = relationship("TaskAffiliation")
