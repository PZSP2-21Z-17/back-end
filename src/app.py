from fastapi import FastAPI

from .routers import index, user

app = FastAPI()
app.include_router(index.router)
app.include_router(user.router, prefix="/user")