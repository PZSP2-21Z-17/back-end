from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import String

from src.db.database import BaseModel

class Subject(BaseModel):
    __tablename__   = 'subject'
    subject_code    = Column(String(5), primary_key=True, nullable=False),
    name            = Column(String(40), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    exams               = relationship("Exam"),
    user_affiliations   = relationship("UserAffiliation")
