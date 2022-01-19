from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, VARCHAR

from src.db.database import BaseModel as BaseSchema

class User(BaseSchema):
    __tablename__   = 'user'
    # Main fields
    user_id         = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name      = Column(VARCHAR(20), nullable=False)
    last_name       = Column(VARCHAR(25), nullable=False)
    password        = Column(VARCHAR(40), nullable=False)
    e_mail          = Column(VARCHAR(50), nullable=False, unique=True)

    # Children
    exams           = relationship("Exam", back_populates='user')
    tasks           = relationship("Task", back_populates='user')
