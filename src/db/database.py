from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

database = create_engine('sqlite://', connect_args = {"check_same_thread": False}, poolclass=StaticPool)

databaseSessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=database)

BaseModel = declarative_base()