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

PLACEHOLDERS = 30


def date_lerp(min, max, t, fmt='%d-%m-%Y'):
    min = mktime(strptime(min, fmt))
    max = mktime(strptime(max, fmt))
    return datetime.fromtimestamp(min + (max - min) * t)


def fill():
    db: Session = databaseSessionMaker()
    # Add to database here

    #
    # Users
    #

    uuids = [
        '0b851b8b-2dfe-452b-9e06-968700cbbc72',
        'e6912348-3270-422d-814f-e516b1af600a',
        '7aac0ee0-6ac2-4854-9db6-5438793b0ea9',
        '48b3d9d0-e1a4-4596-bbe9-888568829a98'
    ]
    user_fields = ['user_id', 'password', 'first_name', 'last_name', 'e_mail']
    user_data = [
        ['ph', 'Place', 'Holder', 'placeholder@gmail.com'],
        ['js', 'Janusz', 'Szczepański', 'jszczep@gmail.com'],
        ['ag', 'Adam', 'Górecki', 'agor@gmail.com'],
        ['ju', 'Julian', 'Urbański', 'jurban@gmail.com'],
    ]
    for (uuid, d) in zip(uuids, user_data):
        db_user = User(**dict(zip(user_fields, [uuid, *d])))
        db.add(db_user)

    #
    # Subject
    #

    subject_fields = ['subject_code', 'name']
    subject_data = [
        ['PLHD', 'Placeholder'],
        ['MATH', 'Mathematic'],
        ['LIT', 'Literature'],
        ['AUTO', 'Automation'],
        ['HIS', 'History'],
        ['REL', 'Religion'],
        ['IT', 'Information Technology'],
        ['GEO', 'Geography'],
        ['PHYS', 'Physics'],
        ['CN', 'Computer Networks']
    ]
    for d in subject_data:
        db_subject = Subject(**dict(zip(subject_fields, d)))
        db.add(db_subject)

    #
    # Exams
    #

    exam_fields = ['date_of_exam', 'content', 'description', 'author_id']
    exam_data = [
        [datetime.strptime('04-12-2021', '%d-%m-%Y'), 'Exam 1', 'Literature, history, religion and geography', uuids[2]],
        [datetime.strptime('13-01-2022', '%d-%m-%Y'), 'Exam 2', 'Mathematics, Physics and Information Technology', uuids[2]],
    ]
    for d in exam_data:
        db_exam = Exam(**dict(zip(exam_fields, d)))
        db.add(db_exam)

    #
    # Groups
    #

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

    #
    # Tasks
    #

    task_fields = ['content', 'date_creation', 'is_visible', 'subject_code', 'author_id']
    task_data = [
        ["What's `2 + 2`?", 'MATH', uuids[1]],
        [r"What's the approximated value of \(\pi\)?", 'MATH', uuids[1]],
        ["Jake had __4__ chocolates. He ate __1__. How many does he have __now__?", 'MATH', uuids[1]],
        ["A brick weights 1 kg and 1/2 of a brick. How much does a brick weight?", 'MATH', uuids[1]],
        ["What does '*memento mori*' mean?", 'LIT', uuids[2]],
        ["Who discovered **America**?", 'HIS', uuids[2]],
        ["How many animals did Moses bring into The Arc?", 'REL', uuids[2]],
        ["What does '*DevOps*' mean?", 'IT', uuids[1]],
        ["What does '*ORM*' stand for?", 'IT', uuids[1]],
        ["Where is the country of Bhutan?", 'GEO', uuids[3]],
        ["What equation is *Albert Einstein* known for?", 'PHYS', uuids[1]],
        ["What's the equation of position over time?", 'PHYS', uuids[1]],
        ["Find the area of the red triangle. ![image](https://i.imgur.com/Uq92le3.png)", 'MATH', uuids[2]],
        ["Is that Joseph Pilsudski? <br><img src='https://upload.wikimedia.org/wikipedia/commons/3/3b/Jozef_Pilsudski1.jpg' alt='drawing' width='200'/>", 'HIS', uuids[3]],
        ["What's radius of circle with circumference 2*pi?", 'MATH', uuids[1]],
        ["Add 8.563 and 4.8292.", 'MATH', uuids[1]],
        ["I am an odd number. Take away one letter and I become even. What number am I?", 'MATH', uuids[1]],
        ["Sally is 54 years old and her mother is 80, how many years ago was Sally's mother times her age??", 'MATH', uuids[1]],
        ["A ship anchored in a port has a ladder which hangs over the side. The length of the ladder is 200cm, the distance between each rung in 20cm and the bottom rung touches the water. The tide rises at a rate of 10cm an hour. When will the water reach the fifth rung?", 'MATH', uuids[1]],
        ["The day before yesterday I was 25. The next year I will be 28. This is true only one day in a year. What day is my Birthday? ", 'MATH', uuids[1]],
        ["Using only an addition, can you get the number 1000 with five numbers made only out of digit 8 (8, 88, 888 etc.)?", 'MATH', uuids[1]],
        ["A man is climbing up a mountain which is inclined. He has to travel 100 km to reach the top of the mountain. Every day He climbs up 2 km forward in the day time. Exhausted, he then takes rest there at night time. At night, while he is asleep, he slips down 1 km backwards because the mountain is inclined. Cat He reach peak in less than 100 days?", 'MATH', uuids[1]],
        ["Look at this series: 53, 53, 40, 40, 27, 27, … What number should come next", 'MATH', uuids[1]],
        ["Can you get a number 100 by using three sevens (7's) and a one (1)?", 'MATH', uuids[1]],
        ["What is the name of the capital of Sri Lanka?", 'GEO', uuids[3]],
        ["How many states are in USA", 'GEO', uuids[3]],
        ["Is Taiwan a country?", 'GEO', uuids[3]],
        ["What is the official language of Trinidad and Tobago?", 'GEO', uuids[3]],
        ["Is the UK in the EU?", 'GEO', uuids[3]],
        ["Current General Secretary of Chinese Communist Party.", 'HIS', uuids[3]],
        ["What is Obama's last name?", 'HIS', uuids[3]],
        ["Current Prime Minister of the UK.", 'HIS', uuids[3]],
        ["Is Chile in South America", 'GEO', uuids[3]],
        ["What is the product of this code: \n```py\na = 7 - 2\nprint(a)\n```", 'IT', uuids[1]],
        ["What started the great Chicago fire of 1871?", 'HIS', uuids[3]],
        ["The United States bought Alaska from which country?", 'HIS', uuids[3]],
        ["Which of the presidents is not on Mount Rushmore?", 'HIS', uuids[3]],
        ["What is the best-selling novel of all time?", 'HIS', uuids[3]]
    ]
    for _ in range(PLACEHOLDERS):
        task_data.append(["Placeholder.", 'PLHD', uuids[0]])
    task_count = len(task_data)

    [task_contents, task_subject_code, task_author_id] = [list(e) for e in zip(*task_data)]
    task_date_creation = [date_lerp('01-10-2019', '01-12-2021', i / (task_count - 1)) for i in range(task_count)]
    task_is_visible = ['N' if i in (0, 1, 2, 6, 9) else 'Y' for i in range(task_count)]

    for d in zip(task_contents, task_date_creation, task_is_visible, task_subject_code, task_author_id):
        db_task = Task(**dict(zip(task_fields, d)))
        db.add(db_task)

    #
    # Answers
    #

    answer_fields = ['task_id', 'content', 'is_correct']
    answer_data = [
        [
            ("2", 'N'),
            ("4", 'Y'),
            ("6", 'N')
        ],
        [
            ("~3.14", 'Y'),
            ("~2.78", 'N'),
            ("3", 'N'),
            ("4", 'N')
        ],
        [
            ("1", 'N'),
            ("3", 'Y'),
            ("4", 'N')
        ],
        [
            ("1 kg", 'N'),
            ("1 brick", 'Y'),
            ("2 kg", 'Y')
        ],
        [
            ("Reminder of the inevitability of death.", 'Y'),
            ("Make the most of the present time and give little thought to the future.", 'N'),
            ("**Gibberish.**", 'N')
        ],
        [
            ("*Vasco Da Gama*", 'N'),
            ("*Christopher Columbus*", 'Y'),
            ("*Benjamin Franklin*", 'N'),
            ("*Nicole Kidman*", 'N')
        ],
        [
            ("3 858 920", 'N'),
            ("0", 'Y'),
            ("All of them", 'N')
        ],
        [
            ("Development, the creation of software itself. Operations, the deployment and management of software.", 'Y'),
            ("Development Operations, list of procedures used by developers.", 'N'),
            ("Mistake made by a developer, a '*dev oops*'.", 'N')
        ],
        [
            ("'*Object Reliant Modularity*'", 'N'),
            ("'*Object Relational Mapping*'", 'Y'),
            ("'*Objective Research Management*'", 'N')
        ],
        [
            ("Asia", 'Y'),
            ("Africa", 'N'),
            ("Europe", 'N'),
            ("North America", 'N'),
            ("South America", 'N'),
            ("Australia/Oceania", 'N'),
            ("Antarctica", 'N')
        ],
        [
            (r"\(E=mc^{2}\)", 'Y'),
            (r"\(e^{i\pi}=-1\)", 'N'),
            (r"\(a^{2}+b^{2}=c^{2}\)", 'N'),
        ],
        [
            (r"\(p=vt\)", 'Y'),
            (r"\(p=\frac{v}{t}\)", 'N'),
        ],
        [
            ("7", 'N'),
            ("9", 'Y'),
            ("5", 'N'),
            ("11", 'N'),
        ],
        [
            ("No", 'N'),
            ("Yes", 'Y'),
        ],
        [
            ("1", 'Y'),
            ("10", 'N'),
            ("2", 'N'),
            ("0", 'N'),
            ("3", 'N'),
        ],
        [
            ("12.235", 'N'),
            ("13.3922", 'Y'),
            ("12.3922", 'N'),
            ("14.235", 'N'),
            ("14.3864", 'N'),
            ("13.3864", 'N'),
        ],
        [
            ("5", 'N'),
            ("6", 'N'),
            ("7", 'Y'),
            ("8", 'N'),
            ("9", 'N'),
        ],
        [
            ("30 years ago", 'N'),
            ("41 years ago", 'Y'),
            ("52 years ago", 'N'),
        ],
        [
            ("never", 'N'),
            ("in 10h", 'N'),
            ("in 5h", 'Y'),
            ("in 20h", 'N'),
        ],
        [
            ("December 31", 'Y'),
            ("January 1", 'N'),
        ],
        [
            ("Yes", 'Y'),
            ("No", 'N'),
        ],
        [
            ("Yes", 'Y'),
            ("No", 'N'),
        ],
        [
            ("16", 'N'),
            ("27", 'N'),
            ("53", 'N'),
            ("14", 'Y'),
        ],
        [
            ("Yes", 'N'),
            ("No", 'Y'),
        ],
        [
            ("Paris", "N"),
            ("Colombo", "N"),
            ("Sri Jayawardenepura Kotte", "Y")
        ],
        [
            ("50", "Y"),
            ("51", "N")
        ],
        [
            ("Yes", "Y"),
            ("No", "N")
        ],
        [
            ("French", "N"),
            ("English", "Y"),
            ("Spanish", "N")
        ],
        [
            ("Yes", "Y"),
            ("No", "N")
        ],
        [
            ("Zhao Ziyang", "N"),
            ("Jiang Zemin", "N"),
            ("Xi Jinping", "Y"),
            ("Hu Jintao", "N")
        ],
        [
            ("Barack", "N"),
            ("Obama", "Y")
        ],
        [
            ("Margaret Thatcher", "N"),
            ("Theresa May", "N"),
            ("Boris Johnson", "Y")
        ],
        [
            ("Yes", "Y"),
            ("No", "N")
        ],
        [
            ("a", "N"),
            ("7", "N"),
            ("5", "Y"),
            ("2", "N")
        ],
        [
            ("A cow kicking over a lantern", 'N'),
            ("It remains uncertain", 'Y'),
        ],
        [
            ("Canada", 'N'),
            ("Russia", 'Y'),
            ("China", 'N'),
        ],
        [
            ("Donald Trump", 'Y'),
            ("George Washington", 'N'),
            ("Abraham Lincoln", 'N'),
        ],
        [
            ("Don Quixote", 'Y'),
            ("Harry Potter", 'N'),
            ("Alchemist", 'N'),
        ]
    ]
    for i in range(task_count - len(answer_data)):
        answer_data.append([("Placeholder right answer", 'Y'), ("Placeholder wrong answer", 'N')])
    for (task_id, contents) in zip(range(1, len(answer_data) + 1), answer_data):
        for (content, is_correct) in contents:
            db_answer = Answer(**dict(zip(answer_fields, [task_id, content, is_correct])))
            db.add(db_answer)

    #
    # Tags
    #

    tag_fields = ['name']
    tag_data = [
        'difficulty easy',
        'difficulty medium',
        'difficulty hard',
        'yes/no answers',
        'unusual question',
        'typical question',
        'funny question',
        'teachers favorite',
        'placeholder tag',
        'unused tag',
    ]
    for d in tag_data:
        db_tag = Tag(**dict(zip(tag_fields, [d])))
        db.add(db_tag)

    #
    # Tag Affiliations
    #

    tag_aff_fields = ['task_id', 'tag_id']
    tag_aff_data = [
        [1, 6],
        [1, 6],
        [2, 6, 8],
        [3, 6],
        [3, 5],
        [1, 6],
        [1, 5],
        [2, 6, 8],
        [1, 5],
        [3, 5],
        [2, 6],
        [1, 5],
        [1, 6],
        [2, 4, 5, 8],
        [1, 6],
        [1, 6],
        [2, 5, 8],
        [2, 5],
        [3, 5],
        [3, 5, 8],
        [2, 4, 5],
        [1, 4, 5],
        [2, 6],
        [3, 4, 5],
        [2, 5, 8],
        [1, 6],
        [3, 4, 8],
        [3, 5],
        [1, 4, 6],
        [1, 6],
        [1, 5],
        [1, 6, 8],
        [1, 4, 6],
        [1, 6],
        [1, 5, 8],
        [2, 6],
        [1, 6],
        [3, 5],
    ]
    for _ in range(task_count - len(tag_aff_data)):
        tag_aff_data.append([9])

    for (task_id, tag_ids) in zip(range(1, len(tag_aff_data) + 1), tag_aff_data):
        for tag_id in tag_ids:
            db_tag = TagAffiliation(**dict(zip(tag_aff_fields, [task_id, tag_id])))
            db.add(db_tag)

    #
    # Task Affiliations
    #

    task_aff_fields = ['exam_id', 'group_nr', 'nr_on_sheet', 'task_id']
    task_aff_data = [
        (1, [
            (1, [5, 7, 10]),
            (2, [10, 6, 5]),
        ]),
        (2, [
            (1, [1, 3, 4, 9]),
            (2, [8, 2, 1, 4]),
        ])
    ]
    for (exam_id, group_nrs) in task_aff_data:
        for (group_nr, task_ids) in group_nrs:
            for (nr_on_sheet, task_id) in zip(range(1, len(task_ids) + 1), task_ids):
                db_task = TaskAffiliation(**dict(zip(task_aff_fields, [exam_id, group_nr, nr_on_sheet, task_id])))
                db.add(db_task)

    #
    # Enough.
    #

    db.commit()
    db.close()
