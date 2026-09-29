from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker ,AsyncSession
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from fastapi import      Depends



load_dotenv()
  

data_url = os.getenv("DATABASE_URL")

engine = create_async_engine(data_url,echo=True)


AsyncSesionLocal = async_sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)



class Base(DeclarativeBase):
    pass



async def get_db():
    db = AsyncSesionLocal()
    try:
        yield db
    finally:
        db.close()
   
   


db_dependency = Annotated [AsyncSession,Depends(get_db)]


async def init_db():
    async with engine.begin() as conn :
        await conn.run_sync(Base.metadata.create_all)
