from typing import Annotated

from fastapi import APIRouter, Depends, Request, status
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, async_session, async_sessionmaker
from my_project.schemas import StatusResponce, User, UserCreate, UserResponce, Pet, PetResponce
from my_project.services import UserService


router = APIRouter()

def get_user_service(request: Request):
    return request.app.state.user_service

type UserServiceDep = Annotated[UserService, Depends(get_user_service)]

async def get_session(request:Request):
    session: async_sessionmaker[AsyncSession] = request.app.state.session
    async with session.begin() as sess:
        yield sess

type SessionDep = Annotated[AsyncSession, Depends(get_session)]

# @router.post('/pet_signup', status_code = 201)
# def pet_signup(pet: Pet):
#     global PETS
#     if pet.pet_id in PETS:
#         raise HTTPException(409)
#     PETS[pet.pet_id] = pet


# @router.get('/pets/all_pets')
# def get_all_pets():
#     return PETS

# @router.get('/pets/{pet_id}')
# def get_pet(pet_id:int):
#     if pet_id not in PETS:
#             raise HTTPException(404)
#     pet =  PETS[pet_id]
#     return PetResponce(
#         name = pet.name,
#         age = pet.age,
#         breed = pet.breed
#     )

@router.get("/status")
def get_status():
    return StatusResponce(status='ok')

@router.post('/signup', status_code = 201)
async def signup(user: UserCreate, user_service:UserServiceDep, session: SessionDep):
    await user_service.signup(user, session)

@router.get("/users/all") #, response_model=list[UserResponce]
async def get_all(user_service:UserServiceDep, session: SessionDep):
    users = await user_service.get_all(session)
    return users

@router.get("/users/{id}")
async def get_user_by_id(id:int, user_service:UserServiceDep, session: SessionDep):
    user = await user_service.get_by_id(id, session)
    return UserResponce(
        name = user.name,
        email = user.email
    )
