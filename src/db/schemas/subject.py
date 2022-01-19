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
    tasks           = relationship("Task", back_populates='subject')
