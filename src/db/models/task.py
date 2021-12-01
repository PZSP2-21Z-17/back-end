from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Numeric, String

from src.db.database import BaseModel

class Task(BaseModel):
    __tablename__   = 'task'
    task_id         = Column(Numeric(5), primary_key=True, nullable=False),
    subject_code    = Column(String(5), ForeignKey('user_affiliation.subject_code'), nullable=False),
    user_nr         = Column(Numeric(3), ForeignKey('user_affiliation.user_nr'), nullable=False),
    contents        = Column(String(500), nullable=False),
    score           = Column(Numeric(2), nullable=False),
    date_creation   = Column(DateTime, nullable=False),
    is_visible      = Column(String(1), nullable=False),

    # Ongoing relationships from this table to table:
    answers             = relationship("Answer"),
    task_affiliations   = relationship("TaskAffiliation"),
    tag_affiliation     = relationship("TagAffiliation")