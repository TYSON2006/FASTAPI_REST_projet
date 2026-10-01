from fastapi import APIRouter,Path,Depends
from shema.task import CreateTasksValidation
from services.task import TaskServies
from db.data_base import db_dependency
from services.dependances import get_current_user
from models._models_users import Users
from fastapi import Depends




tasks_routes = APIRouter(prefix="/Tasks", tags=["Tasks"])



@tasks_routes.post("/create")
async def creat_task(
    body: CreateTasksValidation,
    db: db_dependency,
    current_user: Users = Depends(get_current_user)
):
    service = TaskServies(db)
    return await service.create_task(current_user.id)

@tasks_routes.get("/all")
async def consult_all(
    db: db_dependency,
    current_user: Users = Depends(get_current_user),
    completed: bool | None = None,
    priorities: str | None = None
):
     service = TaskServies(db)
     return await service.create_task(current_user.id)
    


@tasks_routes.get("/{task_id}")
async def consult_one(task_id:int,db:db_dependency,current_user = Depends(get_current_user)):
    services = TaskServies(db)
    return await services.get_one_task(task_id, current_user.id)



@tasks_routes.put("/{task_id}")
async def update_task(task_id:int,body:update_task,db:db_dependency,current_user = Depends(get_current_user)):
    services = TaskServies(db)
    return await services.update_task(task_id,body,current_user.id)




@tasks_routes.patch("/{task_id}/complete")
async   def   complete_task(task_id:int,db:db_dependency,current_user = Depends(get_current_user)):
    services = TaskServies(db)
    return await services.complete_task(task_id,current_user.id) 



@tasks_routes.delete("/{task_id}")
async def delete_task(task_id:int,db:db_dependency,current_user = Depends(get_current_user)):
    services = TaskServies(db)
    return await services.delete_task(task_id,current_user.id)
