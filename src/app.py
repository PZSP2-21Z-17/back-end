from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.schemas import *
from .db.database import BaseModel, database
from .db import dummy
from .routers import *

BaseModel.metadata.drop_all(bind=database)
BaseModel.metadata.create_all(bind=database)
dummy.fill()

app = FastAPI()
app.include_router(answer.router, prefix="/answer")
app.include_router(exam.router, prefix="/exam")
app.include_router(group.router, prefix="/group")
app.include_router(subject.router, prefix="/subject")
app.include_router(tag_aff.router, prefix="/tag_aff")
app.include_router(tag.router, prefix="/tag")
app.include_router(task.router, prefix="/task")
app.include_router(user.router, prefix="/user")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)