from fastapi import FastAPI

from my_project.repositories import UserRepository
from my_project.router import router
from my_project.services import UserService 

from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
     from my_project.db import engine, init_db, session
     #init
     await init_db()
     
     app.state.session = session
     
     yield
     #clear and stop
     engine.dispose()


app = FastAPI(lifespan= lifespan)

user_repository = UserRepository()
app.state.user_service = UserService(user_repository)

app.include_router(router)

