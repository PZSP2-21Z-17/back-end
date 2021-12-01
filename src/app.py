from fastapi import FastAPI

from .db.models import *
from .db.database import BaseModel, database
from .routers import index, user

BaseModel.metadata.create_all(bind=database)

app = FastAPI()
app.include_router(index.router)
app.include_router(user.router, prefix="/user")