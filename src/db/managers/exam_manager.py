from random import sample
from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
from src.db.schemas.task_aff import TaskAffiliation

from src.dependencies import get_db
from src.db.schemas.exam import Exam
from src.db.schemas.group import Group

from src.models.exam import *
from src.models.group import GroupCreate

from src.db.managers.group_manager import GroupManager
from src.db.managers.task_aff_manager import TaskAffiliationManager
from src.models.task_aff import TaskAffiliationCreate

class ExamManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, exam: Exam) -> Exam:
        try:
            self.db.add(exam)
            self.db.commit()
            self.db.refresh(exam)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return exam

    def all(self) -> List[Exam]:
        try:
            exam = self.db.query(Exam).all()
        except DatabaseError as error:
            raise error
        return exam

    def byId(self, exam_id: int):
        try:
            exam = self.db.query(Exam).filter(Exam.exam_id == exam_id).one()
        except DatabaseError as error:
            raise error
        return exam

    def generate(self, exam_generate:ExamGenerate):
        try:
            # Tworzenie egzaminu
            with self.db.begin_nested():
                exam_create = ExamCreate(**exam_generate.dict())
                created_exam = self.db.add(Exam(**exam_create.dict()))

            # Tworzenie grup
            with self.db.begin_nested():
                for i in range(exam_generate.group_count):
                    new_group = GroupCreate(exam_id = created_exam.exam_id, group_nr = i+1)
                    self.db.add(Group(**new_group.dict()))

            # Tworzenie rand task_affiliation
            with self.db.begin_nested():
                for i in range(exam_generate.group_count):
                    tasks_chosen = sample(exam_generate.task_ids, exam_generate.tasks_per_exam)
                    for sheet_nr in range(len(tasks_chosen)):
                        new_task_aff = TaskAffiliationCreate(group_nr = i+1, exam_id = created_exam.exam_id, task_id = tasks_chosen[sheet_nr], nr_on_sheet = sheet_nr + 1)
                        self.db.add(TaskAffiliation(**new_task_aff.dict()))
            self.db.commit()

            return created_exam

        except DatabaseError as error:
            self.db.rollback()
            raise error
