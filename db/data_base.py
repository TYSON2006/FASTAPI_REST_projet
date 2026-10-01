import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

URL = os.getenv("DATABASE_URL")

engine = create_async_engine(URL, echo=True,connect_args={"ssl ":True})

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


db_dependency = Annotated[AsyncSession, Depends(get_db)]


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)