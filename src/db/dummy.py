from datetime import datetime
from time import mktime, strptime
from sqlalchemy.orm.session import Session
from src.db.database import databaseSessionMaker

from .schemas.user import User
from .schemas.subject import Subject
from .schemas.exam import Exam
from .schemas.group import Group
from .schemas.task import Task
from .schemas.answer import Answer
from .schemas.tag import Tag
from .schemas.user_aff import UserAffiliation
from .schemas.tag_aff import TagAffiliation
from .schemas.task_aff import TaskAffiliation
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
        db_user = User(**dict(zip(fields, d)))
        db.add(db_user)
    # Subject
    fields = ['subject_code', 'name']
    data = [
        ['PZSP1', 'Projekt zespołowy 1'],
        ['PZSP2', 'Projekt ZeSPołowy 2'],
        ['PZSP3', 'Kto cie skrzywdził?'],
    ]
    for d in data:
        db_subject = Subject(**dict(zip(fields, d)))
        db.add(db_subject)
    # Exams
    fields = ['exam_id', 'date_of_exam', 'commentary', 'description', 'subject_code', 'author_id']
    data = [
        ['1', datetime.strptime('01-01-2020', '%d-%m-%Y'), 'Kolos 1', 'Alchemy, It is the scientific technique of understanding the structure of matter,', 'PZSP1', '1'],
        ['2', datetime.strptime('02-01-2020', '%d-%m-%Y'), 'Exam 1', 'decomposing it, and then reconstructing it.', 'PZSP2', '3'],
        ['3', datetime.strptime('03-01-2020', '%d-%m-%Y'), 'Bul 1', 'If performed skillfully, it is even possible to create gold out of lead.', 'PZSP3', '2'],
        ['4', datetime.strptime('01-04-2020', '%d-%m-%Y'), 'Kolos 2', 'However, as it is a science, there are some natural principles in place.', 'PZSP1', '4'],
        ['5', datetime.strptime('02-04-2020', '%d-%m-%Y'), 'Exam 2', 'Only one thing can be created from something else of a certain mass.', 'PZSP2', '2'],
        ['6', datetime.strptime('03-04-2020', '%d-%m-%Y'), 'Bul 2', 'This is the Principle of Equivalent Exchange. ', 'PZSP3', '3'],
    ]
    for d in data:

        db_exam = Exam(**dict(zip(fields, d)))
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
        db_group = Group(**dict(zip(fields, d)))
        db.add(db_group)
    # Tasks
    fields = ['task_id', 'contents', 'score', 'date_creation', 'is_visible', 'subject_code', 'author_id']

    task_contents = ['Read 177013',
                    'Hunt down the furries',
                    'Commit Genocide',
                    'Get Adolf some juice', 
                    'Go on a Crusade ', 
                    'Make a Gachi mixtape',
                    'Fight for inhuman rights', 
                    'Abolish the Monarchy', 
                    'Play a game of Dungeons and Dragons', 
                    'See the end',
                    'Enroll wilingly on POFA', 
                    'Become the Dziekan', 
                    'Finish making the archers game in react', 
                    'Give your friend the vodka you owe him', 
                    'Don`t wrestle with SCP-089', 
                    'Finish all terraria bosses in one hour', 
                    'Become the pope for funsies', 
                    'Become the Gachi playlist',
                    'Go on a party with the Pope']
    
    data = [[i, task_contents[i], randint(1, 10), dlerp('01-10-2019', '01-12-2019', random(), '%d-%m-%Y'), 'Y', f'PZSP{randint(1, 3)}', randint(1, 4)] for i in range(1, 19)]
    for d in data:
        db_task = Task(**dict(zip(fields, d)))
        db.add(db_task)
    # Answers
    fields = ['answer_id', 'content', 'is_correct', 'task_id']
    content = ['yes', 'no', 'proceed']
    data = [[i, content[i%3], 'Y' if randint(0, 1) == 1 else 'N', i//3 + 1] for i in range(1, 54)]
    for d in data:
        db_answer = Answer(**dict(zip(fields, d)))
        db.add(db_answer)
    # Tags
    fields = ['tag_id', 'name']
    data = [
        [1, 'hard'],
        [2, 'special'],
        [3, 'exam material'],
        [4, 'easy'],
        [5, '50/50'],
        [6, '100-0'],
        [7, 'no-life'],
        [8, 'yes'],
    ]
    for d in data:
        db_tag = Tag(**dict(zip(fields, d)))
        db.add(db_tag)
    
    # From this point the responsibility for the test data takes the unpaid assistant.

    # User Affiliations
    fields = ['subject_code', 'user_id', 'permission_level']
    data = [
        ['PZSP1', 1, 0],
        ['PZSP2', 1, 0],
        ['PZSP1', 2, 1],
        ['PZSP2', 2, 1],
        ['PZSP3', 2, 2],
        ['PZSP1', 3, 2],
        ['PZSP3', 3, 2],
        ['PZSP3', 4, 2],
    ]
    for d in data:
        db_tag = UserAffiliation(**dict(zip(fields, d)))
        db.add(db_tag)

    # Tag Affiliations
    fields = ['task_id', 'tag_id']
    data = [
        [1, 1],
        [1, 2],
        [2, 1],
        [3, 2],
        [4, 3],
        [5, 4],
        [6, 5],
        [7, 6],
        [7, 7],
        [8, 8],
        [9, 1],
        [10, 2],
        [11, 3],
        [12, 4],
        [13, 5],
        [14, 6],
        [15, 7],
        [16, 8],
        [17, 8],
        [18, 1],
        [18, 2],
        [18, 3],
        [18, 4],
        [18, 5],
        [18, 6],
        [18, 7],
        [18, 8],
    ]
    for d in data:
        db_tag = TagAffiliation(**dict(zip(fields, d)))
        db.add(db_tag)
    # Task Affiliations
    fields = ['nr_on_sheet', 'group_nr', 'exam_id', 'task_id']
    exam_groups = [
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
    # Tasks 18
    # Nr on sheets 1-6
    # Exam groups 12
    data = []
    starting = 0
    for exam in exam_groups:
        for nr_on_sheet in range(1,7):
            d = [nr_on_sheet, exam[0], exam[1], (nr_on_sheet + starting) % 18]
            starting += 1

            db_task = TaskAffiliation(**dict(zip(fields, d)))
            db.add(db_task)

    # Enough.
    db.commit()
    db.close()