from fastapi import HTTPException

from my_project.models import User, UserRole

from my_project.repositories import UserRepository
from my_project.schemas import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository): 
        self.__user_repository = user_repository

    async def signup(self, user: UserCreate):
        all_rep =  await self.__user_repository.get_all()
        emails = [u.email for u in all_rep] 
        if len(all_rep) == 0:
            role = UserRole.ADMIN            
        else:
            role = UserRole.USER 

        model = User(
            id = 0, 
            login = user.login,                name = user.name, 
            role = role,
            email = user.email,
            password = user.password,
        )
        if model.email not in emails:
            await self.__user_repository.save(model)
            return model
        else:
            raise HTTPException(409)

    async def get_by_id(self, id:int):
        model = await self.__user_repository.get_by_id(id)
        if model is None:
            raise HTTPException(404)
        return model
        
    async def get_all(self): 
        return await self.__user_repository.get_all()

        