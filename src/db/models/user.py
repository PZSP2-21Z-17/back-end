from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.sqltypes import Numeric, String

from src.db.database import BaseModel

class User(BaseModel):
    __tablename__   = 'user'
    user_nr         = Column(Numeric(3), primary_key=True, nullable=False)
    first_name      = Column(String(20), nullable=False),
    last_name       = Column(String(25), nullable=False),
    password        = Column(String(40), nullable=False),
    e_mail          = Column(String(50), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    exams               = relationship("Exam"),
    user_affiliations   = relationship("UserAffiliation")


