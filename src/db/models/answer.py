from sqlalchemy import Column
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Numeric, String

from src.db.database import BaseModel

class Answer(BaseModel):
    __tablename__   = 'answer'
    task_id         = Column(Numeric(5), primary_key=True, nullable=False),
    answer_nr       = Column(Numeric(2), ForeignKey('task.task_id'), primary_key=True, nullable=False),
    content         = Column(String(500), nullable=False),
    is_correct      = Column(String(1), nullable=False)   # Właściwie tutaj to string czy bool?
