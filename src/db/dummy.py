import datetime
from time import mktime, strftime, strptime
from sqlalchemy.orm.session import Session
from src.db.database import databaseSessionMaker

from .models.user import User as UserModel
from .models.subject import Subject as SubjectModel
from .models.exam import Exam as ExamModel
from .models.group import Group as GroupModel
from .models.task import Task as TaskModel
from .models.answer import Answer as AnswerModel

from datetime import datetime
from random import randint, random

def dlerp(min, max, t, fmt):
    min = mktime(strptime(min, fmt))
    max = mktime(strptime(max, fmt))
    return datetime.fromtimestamp(min + (max - min) * t)

def fill():
    db: Session = databaseSessionMaker()
    # Add to database here
    # Users
    fields = ['user_id', 'password', 'first_name', 'last_name', 'e_mail']
    data = [
        [1, 'Bartek', 'Bartek', 'Bartek', 'bartek@gmail.com'],
        [2, 'Dawid', 'Dawid', 'Dawid', 'dawid@gmail.com'],
        [3, 'Janek', 'Janek', 'Janek', 'janek@gmail.com'],
        [4, 'Kuba', 'Kuba', 'Kuba', 'kuba@gmail.com'],
    ]
    for d in data:
        db_user = UserModel(**dict(zip(fields, d)))
        db.add(db_user)
    # Subject
    fields = ['subject_code', 'name']
    data = [
        ['PZSP1', 'Projekt zespołowy 1'],
        ['PZSP2', 'Projekt ZeSPołowy 2'],
        ['PZSP3', 'Kto cie skrzywdził?'],
    ]
    for d in data:
        db_subject = SubjectModel(**dict(zip(fields, d)))
        db.add(db_subject)
    # Exams
    fields = ['exam_id', 'date_of_exam', 'commentary', 'subject_code', 'author_id']
    data = [
        ['1', datetime.strptime('01-01-2020', '%d-%m-%Y'), 'Kolos 1', 'PZSP1', '1'],
        ['2', datetime.strptime('02-01-2020', '%d-%m-%Y'), 'Exam 1', 'PZSP2', '3'],
        ['3', datetime.strptime('03-01-2020', '%d-%m-%Y'), 'Bul 1', 'PZSP3', '2'],
        ['4', datetime.strptime('01-04-2020', '%d-%m-%Y'), 'Kolos 2', 'PZSP1', '4'],
        ['5', datetime.strptime('02-04-2020', '%d-%m-%Y'), 'Exam 2', 'PZSP2', '2'],
        ['6', datetime.strptime('03-04-2020', '%d-%m-%Y'), 'Bul 2', 'PZSP3', '3'],
    ]
    for d in data:

        db_exam = ExamModel(**dict(zip(fields, d)))
        db.add(db_exam)
    # Groups
    fields = ['group_nr', 'exam_id']
    data = [
        ['1', '1'],
        ['2', '1'],
        ['1', '2'],
        ['2', '2'],
        ['1', '3'],
        ['2', '3'],
        ['1', '4'],
        ['2', '4'],
        ['1', '5'],
        ['2', '5'],
        ['1', '6'],
        ['2', '6'],
    ]
    for d in data:
        db_group = GroupModel(**dict(zip(fields, d)))
        db.add(db_group)
    # Tasks
    fields = ['task_id', 'contents', 'score', 'date_creation', 'is_visible', 'subject_code', 'author_id']
    data = [[i, 'Raise left hand', randint(1, 10), dlerp('01-10-2019', '01-12-2019', random(), '%d-%m-%Y'), 'Y', randint(1, 3), randint(1, 4)] for i in range(1, 19)]
    for d in data:
        db_task = TaskModel(**dict(zip(fields, d)))
        db.add(db_task)
    # Answers
    fields = ['answer_id', 'content', 'is_correct', 'task_id']
    content = ['yes', 'no', 'proceed']
    data = [[i, content[i%3], 'Y' if randint(0, 1) == 1 else 'N', i//3 + 1] for i in range(1, 73)]
    for d in data:
        db_answer = AnswerModel(**dict(zip(fields, d)))
        db.add(db_answer)
    # Enough.
    db.commit()
    db.close()