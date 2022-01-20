
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm.exc import NoResultFound

ManagerError = (DatabaseError, NoResultFound)
