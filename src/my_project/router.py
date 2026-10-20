from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from my_project.schemas import StatusResponce, User, UserResponce

router = APIRouter()

USERS_DATABASE = dict[str, User]()

@router.post('/signup', status_code = 201)
def signup(user: User):
    global USERS_DATABASE
    if user.login in USERS_DATABASE:
        raise HTTPException(409)
    USERS_DATABASE[user.login] = user


@router.get("/status")
def get_status():
    return StatusResponce(status='ok')


@router.get("/users/{login}")
def get_user(login:str):
    user = USERS_DATABASE[login]
    return UserResponce(
        name = user.name,
        email = user.email,
    )