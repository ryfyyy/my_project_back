from enum import StrEnum

from my_project.db import Base

from pydantic import BaseModel

from sqlalchemy.orm import Mapped, mapped_column
class UserRole(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    role: Mapped[UserRole]