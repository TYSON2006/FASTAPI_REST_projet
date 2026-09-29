from fastapi import FastAPI
from routes.users import users_rooter
from db.data_base import init_db


 



app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()    



app.include_router(users_rooter)