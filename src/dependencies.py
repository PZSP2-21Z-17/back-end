from .db.database import databaseSessionMaker

def get_db():
    db = databaseSessionMaker()
    try:
        yield db
    finally:
        db.close()