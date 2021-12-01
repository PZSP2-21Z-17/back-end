from sqlalchemy.orm.session import Session
from src.db.database import databaseSessionMaker

from .models.user import User as UserModel
from ..schemas.user import UserCreate as UserSchema

def fill():
    db: Session = databaseSessionMaker()
    # Add to database here
    passwords = ['Bartek', 'Dawid', 'Janek', 'Kuba']
    first_names = ['Bartek', 'Dawid', 'Janek', 'Kuba']
    last_names = ['Bartek', 'Dawid', 'Janek', 'Kuba']
    e_mails = ['bartek@gmail.com', 'dawid@gmail.com', 'janek@gmail.com', 'kuba@gmail.com']
    for (p, f, l, e) in zip(passwords, first_names, last_names, e_mails):
        user = UserSchema(password = p, first_name = f, last_name = l, e_mail = e)
        user = UserModel(**user.dict())
        db.add(user)
    # Enough.
    db.commit()
    db.close()