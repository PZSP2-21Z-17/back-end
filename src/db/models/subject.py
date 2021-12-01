from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Text

from src.db.database import BaseModel

class Subject(BaseModel):
    __tablename__   = 'subject'
    # Main fields
    subject_code    = Column(Text(5), primary_key=True, nullable=False)
    name            = Column(Text(40), nullable=False, unique=True)
