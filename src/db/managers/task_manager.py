from typing import List
from uuid import UUID
from fastapi import Depends
from sqlalchemy import func, select, literal_column, String, literal
from sqlalchemy.sql import label, case, any_, desc, cast, or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from src.dependencies import get_db
from src.db.schemas.task import Task
from src.db.schemas.answer import Answer
from src.db.schemas.tag_aff import TagAffiliation
from src.db.schemas.tag import Tag
from src.db.schemas.subject import Subject

from src.models.task import TaskBase, TaskCreateWithTagsAnswers, TaskModel, TaskCreate

class TaskManager:
    def __init__ (self, db: Session = Depends(get_db)):
        self.db = db

    def add(self, task: Task) -> Task:
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return task

    def all(self, user_id: UUID) -> List[Task]:
        try:
            tasks = self.db.query(Task).filter((Task.is_visible == 'Y') | (Task.author_id == user_id)).all()
        except DatabaseError as error:
            raise error
        return tasks

    def byId(self, user_id: UUID, task_id: int):
        try:
            answer = self.db.query(Task).filter((Task.is_visible == 'Y') | (Task.author_id == user_id)).filter(Task.task_id == task_id).one()
        except DatabaseError as error:
            raise error
        return answer

    def delete(self, user_id: UUID, task: TaskBase):
        try:
            query = self.db.query(Task).\
                filter(Task.task_id == task.task_id).\
                filter(Task.author_id == user_id)
            if query.filter(~Task.task_affs.any()).first() is not None:
                query.delete()
                self.db.commit()
                return
            else:
                raise DatabaseError()
        except DatabaseError as error:
            raise error

    def update(self, user_id: UUID, task:TaskModel):
        try:
            self.db.query(Task).filter(Task.task_id == task.task_id).filter(Task.author_id == user_id).update(task.dict())
            self.db.commit()
            db_task = self.db.query(Task).filter(Task.task_id == task.task_id).one()
        except DatabaseError as error:
            raise error
        return db_task

    def one_with_answers(self, user_id: UUID, task_id: int):
        try:
            task = self.db.query(Task).filter(Task.task_id == task_id).filter((Task.is_visible == 'Y') | (Task.author_id == user_id)).one()
        except DatabaseError as error:
            raise error
        return task

    def all_with_answers(self, user_id: UUID):
        try:
            tasks = self.db.query(Task).filter((Task.is_visible == 'Y') | (Task.author_id == user_id)).all()
        except DatabaseError as error:
            raise error
        return tasks

    def create_with_tags_answers(self, task_with_answers: TaskCreateWithTagsAnswers):
        task = TaskCreate(**task_with_answers.dict())
        db_task = Task(**task.dict())
        db_answers = [Answer(**answer.dict()) for answer in task_with_answers.answers]
        db_tags = [Tag(**tag.dict()) for tag in task_with_answers.tags]
        try:
            self.db.add(db_task)
            for db_answer in db_answers:
                db_task.answers.append(db_answer)
            for db_tag in db_tags:
                db_task.tags.append(db_tag)
            self.db.commit()
            self.db.refresh(db_task)
        except DatabaseError as error:
            self.db.rollback()
            raise error
        return db_task
    
    def find(self, user_id: UUID, tags: List[int], search_string: str = None, subject_code: str = None, offset: int = 0, limit: int = 25):
        try:
            query = self.db.query(Task, Task.task_affs.any().label('in_use')).\
                filter((Task.is_visible == 'Y') | (Task.author_id == user_id))
            if len(tags) > 0:
                query = query.\
                    join(Task.tag_affs).\
                    filter(TagAffiliation.tag_id.in_(tags)).\
                    group_by(Task).\
                    having(func.count() == len(tags))
            if subject_code is not None:
                query = query.filter(Task.subject_code == subject_code)
            if search_string is not None:
                query = query.\
                    filter(func.similarity(Task.content, search_string) > 0.001).\
                    order_by(desc(func.similarity(Task.content, search_string)))
            query = query.limit(limit).offset(offset*limit)
            return query.all()
        except DatabaseError as error:
            raise error

    def search_tips(self, search_string: str, offset: int = 0, limit: int = 25):
        try:
            subjects = self.db.query(
                literal('subject').label('type'),
                label('id', Subject.subject_code),
                label('name', Subject.name)
            )
            tags = self.db.query(
                literal('tag').label('type'),
                label('id', cast(Tag.tag_id, String)),
                label('name', Tag.name)
            )
            query = subjects.union(tags).\
                filter(func.similarity(literal_column('name'), search_string) > 0.001).\
                order_by(desc(func.similarity(literal_column('name'), search_string))).\
                limit(limit).\
                offset(offset*limit)
            return query.all()
        except DatabaseError as error:
            raise error
