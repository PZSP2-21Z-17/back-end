from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database = create_engine('sqlite://', connect_args = {"check_same_thread": False})

databaseSession = sessionmaker(autocommit=False, autoflush=False, bind=database)

baseModel = declarative_base()