from fastapi import FastAPI

from .routers import index, user
from .db.database import BaseModel, database

BaseModel.metadata.create_all(bind=database)

app = FastAPI()
app.include_router(index.router)
app.include_router(user.router, prefix="/user")