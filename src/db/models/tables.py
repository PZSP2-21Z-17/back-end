from sqlalchemy import Column, Integer
from sqlalchemy.orm import relation, relationship, relationships
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String

from src.db.database import BaseModel

# 1. Create basic tables with primary keys (done)
# 2. Set not null on tables and primary keys (done)
# 2.2 Set index on tables and columns
# 3. Set foreign keys (done)
# 4. Add indexes
# 5. Add triggers for non transfarabble fk

class Exam(BaseModel):
    __tablename__   = 'exam'
    nr_exam         = Column(Integer(5), primary_key=True, nullable=False),
    code_subject    = Column(String(5), ForeignKey('subject.code_subject'), primary_key=True, nullable=False),
    nr_user         = Column(Integer(3), ForeignKey('user.nr_user'), nullable=False),
    date_of_exam    = Column(DateTime, nullable=False),
    commentary      = Column(String(100)),

    # Ongoing relationships from this table to table:
    groups              = relationship("Group")

class Group(BaseModel):
    __tablename__   = 'group'
    nr_group        = Column(Integer(5), primary_key=True, nullable=False), 
    nr_exam         = Column(Integer(5), ForeignKey('exam.nr_exam'), primary_key=True, nullable=False),
    code_subject    = Column(String(5), ForeignKey('exam.code_subject'), primary_key=True, nullable=False),
    nr_user         = Column(Integer(3), ForeignKey('exam.nr_user'), primary_key=True, nullable=False),

    # Ongoing relationships from this table to table:
    task_affiliations   = relationship("TaskAffiliation")

class Answer(BaseModel):
    __tablename__   = 'answer'
    id_task         = Column(Integer(5), primary_key=True, nullable=False),
    nr_answer       = Column(Integer(2), ForeignKey('task.id_task'), primary_key=True, nullable=False),
    content         = Column(String(500), nullable=False),
    is_correct      = Column(String(1), nullable=False)   # Właściwie tutaj to string czy bool?

class Subject(BaseModel):
    __tablename__   = 'subject'
    code_subject    = Column(String(5), primary_key=True, nullable=False),
    name            = Column(String(40), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    exams               = relationship("Exam"),
    user_affiliations   = relationship("UserAffiliation")

class TaskAffiliation(BaseModel):
    __tablename__   = "task_affiliation"
    nr_on_sheet     = Column(Integer(5), nullable=False),
    id_task         = Column(Integer(5), ForeignKey('task.id_task'), primary_key=True, nullable=False),
    nr_exam         = Column(Integer(5), ForeignKey('group.nr_exam'), primary_key=True, nullable=False),
    code_subject    = Column(String(5), ForeignKey('group.code_subject'), primary_key=True, nullable=False),
    nr_group        = Column(Integer(5), ForeignKey('group.nr_group'), primary_key=True, nullable=False),
    nr_user         = Column(Integer(3), ForeignKey('group.nr_user'), primary_key=True, nullable=False)

class TagAffiliation(BaseModel):
    __tablename__   = 'tag_affiliation'
    id_task         = Column(Integer(5), ForeignKey('task.id_task'), primary_key=True, nullable=False),
    code_tag        = Column(String(5), ForeignKey('tag.code_tag'), primary_key=True, nullable=False)

class UserAffiliation(BaseModel):
    __tablename__   = 'user_affiliation'
    code_subject    = Column(String(5), ForeignKey('subject.code_subject'), primary_key=True, nullable=False),
    nr_user         = Column(Integer(3), ForeignKey('user.nr_user'), primary_key=True, nullable=False),

    # Ongoing relationships from this table to table:
    tasks               = relationship("Task")

class Task(BaseModel):
    __tablename__   = 'task'
    id_task         = Column(Integer(5), primary_key=True, nullable=False),
    code_subject    = Column(String(5), ForeignKey('user_affiliation.code_subject'), nullable=False),
    nr_user         = Column(Integer(3), ForeignKey('user_affiliation.nr_user'), nullable=False),
    contents        = Column(String(500), nullable=False),
    score           = Column(Integer(2), nullable=False),
    date_creation   = Column(DateTime, nullable=False),
    is_visible      = Column(String(1), nullable=False),

    # Ongoing relationships from this table to table:
    answers             = relationship("Answer"),
    task_affiliations   = relationship("TaskAffiliation"),
    tag_affiliation     = relationship("TagAffiliation")

class Tag(BaseModel):
    __tablename__   = 'tag'
    code_tag        = Column(String(5), primary_key=True, nullable=False),
    name            = Column(String(20), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    tag_affiliations    = relationship("TagAffiliation")

class User(BaseModel):
    __tablename__   = 'user'
    nr_user         = Column(Integer(3), primary_key=True, nullable=False)
    first_name      = Column(String(20), nullable=False),
    last_name       = Column(String(25), nullable=False),
    password        = Column(String(40), nullable=False),
    e_mail          = Column(String(50), nullable=False, unique=True),

    # Ongoing relationships from this table to table:
    exams               = relationship("Exam"),
    user_affiliations   = relationship("UserAffiliation")






