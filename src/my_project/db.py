from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlalchemy.orm import DeclarativeBase

DB_URL = 'sqlite+aiosqlite:///my_project.db'

engine = create_async_engine(DB_URL)

session = async_sessionmaker(engine)

class Base(DeclarativeBase): ...


async def init_db():
    from my_project.models import User #noqa: F401
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)