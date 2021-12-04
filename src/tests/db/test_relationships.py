from src.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


### Tu coś z tym zrobic może

def test_subject_relationships(db: Session = Depends(get_db)):
    from src.db.models.subject import Subject
    subject = db.query(Subject).first()
    # Relationship with `Exam`
    exams = subject.exams
    assert exams is not None
    assert len(exams) > 0
    # Relationship with `UserAffiliation`
    user_affiliations = subject.user_affiliations
    assert user_affiliations is not None
    assert len(user_affiliations) > 0