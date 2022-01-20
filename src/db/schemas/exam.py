from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, VARCHAR
from sqlalchemy.dialects.postgresql import UUID

from src.db.database import BaseModel as BaseSchema

class Exam(BaseSchema):
    __tablename__   = 'exam'
    # Main fields
    exam_id         = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    date_of_exam    = Column(DateTime, nullable=False)
    content         = Column(VARCHAR(100))
    description     = Column(VARCHAR(2000))
    # Parents
    author_id       = Column(UUID(as_uuid=True), ForeignKey('user.user_id'), nullable=False)
    user            = relationship("User", back_populates='exams')

    # Children
    groups          = relationship("Group", back_populates='exams')
