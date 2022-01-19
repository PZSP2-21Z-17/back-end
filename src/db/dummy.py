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
from .schemas.tag_aff import TagAffiliation
from .schemas.task_aff import TaskAffiliation
from random import randint, random

def date_lerp(min, max, t, fmt = '%d-%m-%Y'):
    min = mktime(strptime(min, fmt))
    max = mktime(strptime(max, fmt))
    return datetime.fromtimestamp(min + (max - min) * t)

def fill():
    db: Session = databaseSessionMaker()
    # Add to database here



    # Users
    user_fields = ['password', 'first_name', 'last_name', 'e_mail']
    user_data = [
        ['ph', 'Place', 'Holder', 'placeholder@gmail.com'],
        ['js', 'Janusz', 'Szczepański', 'jszczep@gmail.com'],
        ['ag', 'Adam', 'Górecki', 'agor@gmail.com'],
        ['ju', 'Julian', 'Urbański', 'jurban@gmail.com'],
    ]
    for d in user_data:
        db_user = User(**dict(zip(user_fields, d)))
        db.add(db_user)



    # Subject
    subject_fields = ['subject_code', 'name']
    subject_data = [
        ['PLHD', 'Placeholder'],
        ['MATH', 'Mathematic'],
        ['LIT', 'Literature'],
        ['HIS', 'History'],
        ['REL', 'Religion'],
        ['IT', 'Information Technology'],
        ['GEO', 'Geography'],
    ]
    for d in subject_data:
        db_subject = Subject(**dict(zip(subject_fields, d)))
        db.add(db_subject)



    # Exams
    exam_fields = ['date_of_exam', 'commentary', 'description', 'author_id']
    exam_data = [
        [datetime.strptime('04-12-2021', '%d-%m-%Y'), 'Exam 1', 'Literature, history, religion and geography', 3],
        [datetime.strptime('13-01-2022', '%d-%m-%Y'), 'Exam 2', 'Mathematics and Information Technology', 3],
    ]
    for d in exam_data:
        db_exam = Exam(**dict(zip(exam_fields, d)))
        db.add(db_exam)



    # Groups
    group_fields = ['exam_id', 'group_nr']
    group_data = [
        ['1', '1'],
        ['1', '2'],
        ['2', '1'],
        ['2', '2'],
    ]
    for d in group_data:
        db_group = Group(**dict(zip(group_fields, d)))
        db.add(db_group)



    task_fields = ['contents', 'date_creation', 'is_visible', 'subject_code', 'author_id']
    task_data = [
        ["What's 2 + 2?", 'MATH', 2],
        ["What's the approximated value of π?", 'MATH', 2],
        ["Jake had 4 chocolates. He ate 1. How many does he have now?", 'MATH', 2],
        ["A brick weights 1 kg and 1/2 of a brick. How much does a brick weight?", 'MATH', 2],
        ["What does 'memento mori' mean?", 'LIT', 3],
        ["Who discovered America?",'HIS', 3],
        ["How many animals did Moses bring into The Arc?", 'REL', 3],
        ["What does DevOps mean?", 'IT', 2],
        ["What does ORM stand for?", 'IT' , 2],
        ["On which continent is the country of Bhutan?", 'GEO', 4]
    ]
    for _ in range(20):
        task_data.append(["Placeholder.", 'PLHD', 1])
    task_count = len(task_data)

    [task_contents, task_subject_code, task_author_id] = [list(e) for e in zip(*task_data)]
    task_date_creation = [date_lerp('01-10-2019', '01-12-2021', i / (task_count - 1)) for i in range(task_count)]
    task_is_visible = ['Y' if i % 2 == 0 else 'N' for i in range(task_count)]
    
    for d in zip(task_contents, task_date_creation, task_is_visible, task_subject_code, task_author_id):
        db_task = Task(**dict(zip(task_fields, d)))
        db.add(db_task)



    # Answers
    fields = ['answer_id', 'content', 'is_correct', 'task_id']
    content = ['yes', 'no', 'proceed']
    data = [[i, content[i%3], 'Y' if randint(0, 1) == 1 else 'N', i//3 + 1] for i in range(1, 54)]
    for d in data:
        db_answer = Answer(**dict(zip(fields, d)))
        db.add(db_answer)



    # Tags
    tag_fields = ['name']
    tag_data = [
        'easy',
        'medium',
        'hard',
        'yes/no',
        'unusual',
        'typical',
        'teachers favorite',
        'placeholder'
    ]
    for d in tag_data:
        db_tag = Tag(**dict(zip(tag_fields, [d])))
        db.add(db_tag)



    # Tag Affiliations
    tag_aff_fields = ['task_id', 'tag_id']
    tag_aff_data = [
        [1, [1, 6]],
        [2, [1, 6]],
        [3, [2, 6, 7]],
        [4, [3, 6]],
        [5, [3, 5]],
        [6, [1, 6]],
        [7, [1, 5]],
        [8, [2, 6, 7]],
        [9, [1, 5]],
        [10, [3, 5]]
    ]
    for i in range(20):
        tag_aff_data.append([11+i, [8]])

    for (task_id, tag_ids) in tag_aff_data:
        for tag_id in tag_ids:
            db_tag = TagAffiliation(**dict(zip(tag_aff_fields, [task_id, tag_id])))
            db.add(db_tag)



    # Task Affiliations
    task_aff_fields = ['exam_id', 'group_nr', 'nr_on_sheet', 'task_id']
    task_aff_data = [
        (
            1,
            [
                (1, [5, 7, 10]),
                (2, [10, 6, 5]),
            ]
        ),
        (
            2,
            [
                (1, [1, 3, 4, 9]),
                (2, [8, 2, 1, 4]),
            ]
        )
    ]
    for (exam_id, group_nrs) in task_aff_data:
        for (group_nr, task_ids) in group_nrs:
            for (nr_on_sheet, task_id) in zip(range(1, len(task_ids)+1), task_ids):
                db_task = TaskAffiliation(**dict(zip(task_aff_fields, [exam_id, group_nr, nr_on_sheet, task_id])))
                db.add(db_task)

    # Enough.
    db.commit()
    db.close()