from sqlalchemy import Column, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.dialects.postgresql import UUID

from src.db.database import BaseModel as BaseSchema


class User(BaseSchema):
    __tablename__   = 'user'
    # Main fields
    user_id         = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    first_name      = Column(VARCHAR(20), nullable=False)
    last_name       = Column(VARCHAR(25), nullable=False)
    password        = Column(VARCHAR(40), nullable=False)
    e_mail          = Column(VARCHAR(50), nullable=False, unique=True)

    # Children
    exams           = relationship("Exam", back_populates='user')
    tasks           = relationship("Task", back_populates='user')
