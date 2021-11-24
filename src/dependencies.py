from .db.database import databaseSession

def get_db():
    db = databaseSession()
    try:
        yield db
    finally:
        db.close()