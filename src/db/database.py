import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://app:app@localhost:54321/app')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
database = create_engine(DATABASE_URL, poolclass=StaticPool)

databaseSessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=database)

BaseModel = declarative_base()
