from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import VARCHAR

from src.db.database import BaseModel as BaseSchema

class Subject(BaseSchema):
    __tablename__   = 'subject'
    # Main fields
    subject_code    = Column(VARCHAR(5), primary_key=True, nullable=False)
    name            = Column(VARCHAR(40), nullable=False, unique=True)

    # Children 
    user_affs       = relationship("UserAffiliation", back_populates='subjects')
    exams           = relationship("Exam", back_populates='subjects')
    tasks           = relationship("Task", back_populates='subjects')

    # That Many-To-Many
    users           = relationship("User", secondary='user_affiliation', back_populates='subjects', overlaps="user_affs")

