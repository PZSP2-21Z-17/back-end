from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text

from src.db.database import BaseModel

class Answer(BaseModel):
    __tablename__   = 'answer'
    # Main fields
    answer_id       = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    content         = Column(Text(500), nullable=False)
    is_correct      = Column(Text(1), nullable=False)

    # Parents
    task_id         = Column(Integer, ForeignKey('task.task_id'), nullable=False)
    tasks           = relationship("Task", back_populates='answers')