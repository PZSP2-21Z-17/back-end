from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, Text

from src.db.database import BaseModel

class Task(BaseModel):
    __tablename__   = 'task'
    # Main fields
    task_id         = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    contents        = Column(Text(500), nullable=False)
    score           = Column(Integer, nullable=False)
    date_creation   = Column(DateTime, nullable=False)
    is_visible      = Column(Text(1), nullable=False)

    # Parents
    subject_code    = Column(Text(5), ForeignKey('subject.subject_code'), nullable=False)
    subjects        = relationship("Subject", back_populates='tasks')
    
    author_id       = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    users           = relationship("User", back_populates='tasks')

    # Children 
    task_affs       = relationship("TaskAffiliation", back_populates='tasks')
    answers         = relationship("Answer", back_populates='tasks')
    tag_affs        = relationship("TagAffiliation", back_populates='tasks')