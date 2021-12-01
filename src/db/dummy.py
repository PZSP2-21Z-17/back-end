from sqlalchemy.orm.session import Session
from src.db.database import databaseSessionMaker

def fill():
    db: Session = databaseSessionMaker()
    # Add to database here

    # Enough.
    db.close()