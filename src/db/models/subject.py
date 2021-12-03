from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Text

from src.db.database import BaseModel

class Subject(BaseModel):
    __tablename__   = 'subject'
    # Main fields
    subject_code    = Column(Text(5), primary_key=True, nullable=False)
    name            = Column(Text(40), nullable=False, unique=True)

    # Children 
    user_affs       = relationship("UserAffiliation", back_populates='subjects')
    exams           = relationship("Exam", back_populates='subjects')
    tasks           = relationship("Task", back_populates='subjects')

