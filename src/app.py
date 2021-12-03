from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.models import *
from .db.database import BaseModel, database
from .db import dummy
from .routers import user, group, tag

BaseModel.metadata.create_all(bind=database)
dummy.fill()

app = FastAPI()
app.include_router(user.router, prefix="/user")
app.include_router(group.router, prefix="/group")
app.include_router(tag.router, prefix="/tag")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)