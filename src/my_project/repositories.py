from sqlalchemy import select

from my_project.models import User

from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    def __init__(self): ... 
        # self.__last_id = 0
        # self.__table = dict[int, User]()

    async def save(self, user:User, session: AsyncSession): 
        session.add(user)
        await session.commit()

    async def get_by_id(self, id:int, session: AsyncSession) :
         return await session.get(User, id)

    async def get_all(self, session: AsyncSession): 
        # return list(self.__table.values())
        q = select(User).order_by(User.id)
        s = await session.execute(q)
        return list(s.scalars().all())

