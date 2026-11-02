from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from my_project.schemas import StatusResponce, User, UserResponce, Pet, PetResponce

router = APIRouter()

USERS_DATABASE = dict[str, User]()

PETS = dict[int, Pet]()

@router.post('/signup', status_code = 201)
def signup(user: User):
    global USERS_DATABASE
    if user.login in USERS_DATABASE:
        raise HTTPException(409)
    USERS_DATABASE[user.login] = user

@router.post('/pet_signup', status_code = 201)
def pet_signup(pet: Pet):
    global PETS
    if pet.pet_id in PETS:
        raise HTTPException(409)
    PETS[pet.pet_id] = pet


@router.get('/pets/all_pets')
def get_all_pets():
    return PETS

@router.get('/pets/{pet_id}')
def get_pet(pet_id:int):
    if pet_id not in PETS:
            raise HTTPException(404)
    pet =  PETS[pet_id]
    return PetResponce(
        name = pet.name,
        age = pet.age,
        breed = pet.breed
    )

@router.get("/status")
def get_status():
    return StatusResponce(status='ok')

@router.get("/users/{login}")
def get_user(login:str):
    if login not in USERS_DATABASE:
        raise HTTPException(404)
    user = USERS_DATABASE[login]
    return UserResponce(
        name = user.name,
        email = user.email,
    )