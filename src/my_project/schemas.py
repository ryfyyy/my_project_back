import email

from pydantic import BaseModel

class StatusResponce(BaseModel):
    status: str

class UserResponce(BaseModel):
    name:str
    email:str

class User(BaseModel):
    login: str
    name: str
    email: str
    password: str