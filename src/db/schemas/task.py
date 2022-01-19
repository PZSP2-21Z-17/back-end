from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, VARCHAR, CHAR

from src.db.database import BaseModel as BaseSchema

class Task(BaseSchema):
    __tablename__   = 'task'
    # Main fields
    task_id         = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    content         = Column(VARCHAR(500), nullable=False)
    date_creation   = Column(DateTime, nullable=False)
    is_visible      = Column(CHAR(1), nullable=False)

    # Parents
    subject_code    = Column(VARCHAR(5), ForeignKey('subject.subject_code'), nullable=False)
    subject         = relationship("Subject", back_populates='tasks')
    
    author_id       = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    user            = relationship("User", back_populates='tasks')

    # Children 
    task_affs       = relationship("TaskAffiliation", back_populates='tasks')
    answers         = relationship("Answer", back_populates='tasks')
    tag_affs        = relationship("TagAffiliation", back_populates='tasks')
    tags            = relationship("Tag", secondary='tag_affiliation', back_populates='tasks', overlaps="tag_affs,tags,tasks")