from fastapi import HTTPException

from my_project.models import User, UserRole

from my_project.repositories import UserRepository
from my_project.schemas import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

class UserService:
    def __init__(self, user_repository: UserRepository): 
        self.__user_repository = user_repository

    async def signup(self, user: UserCreate, session: AsyncSession):
        all_rep =  await self.__user_repository.get_all(session)
        emails = [u.email for u in all_rep] 
        if len(all_rep) == 0:
            role = UserRole.ADMIN            
        else:
            role = UserRole.USER 

        model = User(
            # id = 0, 
            login = user.login,                
            name = user.name, 
            role = role,
            email = user.email,
            password = user.password,
        )
        if model.email not in emails:
            await self.__user_repository.save(model, session)
            return model
        else:
            raise HTTPException(409)

    async def get_by_id(self, id:int, session:AsyncSession):
        model = await self.__user_repository.get_by_id(id, session)
        if model is None:
            raise HTTPException(404)
        return model
        
    async def get_all(self, session:AsyncSession): 
        return await self.__user_repository.get_all(session)

        