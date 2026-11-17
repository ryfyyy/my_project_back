import email
from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints

class StatusResponce(BaseModel):
    status: str

class UserResponce(BaseModel):
    name:str
    email:str
    # model_config = {"from_attributes": True}

class UserCreate(BaseModel):
    login: Annotated[str, StringConstraints(min_length = 1)]
    name: Annotated[str, StringConstraints(min_length = 1)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length = 6, max_length = 32)]

class User(BaseModel):
    login: str
    name: str
    email: str
    password: str

class Pet(BaseModel):
    pet_id: int
    name: str
    age: int
    breed: str

class PetResponce(BaseModel):
    name: str
    age: int
    breed: str
