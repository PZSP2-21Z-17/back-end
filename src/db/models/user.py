from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, Text

from src.db.database import BaseModel

class User(BaseModel):
    __tablename__   = 'user'
    # Main fields
    user_id         = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name      = Column(Text(20), nullable=False)
    last_name       = Column(Text(25), nullable=False)
    password        = Column(Text(40), nullable=False)
    e_mail          = Column(Text(50), nullable=False, unique=True)

    # Children 
    user_affs       = relationship("UserAffiliation", back_populates='users', overlaps="users")
    exams           = relationship("Exam", back_populates='users')
    tasks           = relationship("Task", back_populates='users')

    # That Many-To-Many
    subjects        = relationship("Subject", secondary='user_affiliation', back_populates='users', overlaps="user_affs,users,subjects")
