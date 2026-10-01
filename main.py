from fastapi import FastAPI
from routes.users import   users_router
from db.data_base import init_db
from routes.task import tasks_routes


 



app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()    



app.include_router(users_router)
app.include_router(tasks_routes)