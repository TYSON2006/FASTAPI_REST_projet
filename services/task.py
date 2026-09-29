from models._models_users import Users 
from db.data_base import db_dependency 
from loguru import logger 
from fastapi import HTTPException
from sqlalchemy import select
from shema .task import CreateTasksValidation
from models._models_task import Tasks


class TaskServies:
    def __init__(self,db=db_dependency):
        self.db = self.db


        async def add_task(self , body_task:CreateTasksValidation,user_id:int) :
            
            nouvelle_taches = CreateTasksValidation(
                
                title = body_task.tilte,
                description= body_task.description,
                completed= body_task.description,
                priorities= body_task.priorities,
                user_id = body_task.user_id
                
            )
            
            self.db.add(nouvelle_taches)
            await self.db.commit()
            await self.db.refresh()
            logger.info("task insert successfully")
            return nouvelle_taches
            
        
        async def get_all_task(self,user_id:int):
            
            result = await  self.db.execute(
                select(CreateTasksValidation).where(CreateTasksValidation.user_id == user_id)
            )
            
            
            task = result.scalar_one_or_one()
            if task is None:
                raise HTTPException(status_code=404,detail="task not found please try again")
            return task
        
        
        
        async def update_all_task(self,user_id:int,body_task:CreateTasksValidation):
            
            result = await self.db.execute(select(CreateTasksValidation).where(CreateTasksValidation.user_id ==user_id,CreateTasksValidation.id == task_id) )
                                         
                                          
            
            
            task = result.scalar_one_or_none()
            
            if task is None:
                raise  HTTPException(status_code=404,detail=" task not found your are autorised")   
            
            task.title = body_task.title,
            task.description = body_task.description,
            task.prirorities = body_task.priorities,
            task.completed = body_task.completed
            
            await self.db.commit()
            await self.db.refresh(task)
            logger.info("task update successfully")
            
            return task
        
        async def delete_task(self,user_id: int, task_id:int):
            result = await select.db.execute(select(CreateTasksValidation).where(CreateTasksValidation.id == user_id,CreateTasksValidation.id ==task_id))
                                             
                                            
            task = result.scalar_one_or_none()
            
            if not task:
                raise HTTPException(status_code=404,detail=" task does not exist")
            
            
            await self.db.commit()
            await self.db.refresh(task)
            logger.info("task update successfully")
            return task
        
        async def filter_task(self,user_id:int ,status:bool):
            result = await self.db.execute(select(CreateTasksValidation).where(CreateTasksValidation.user_id ==user_id,CreateTasksValidation.id ==task_id))
            
            task = result.scalar.all()
            
            if not task:
                raise HTTPException(status_code=404,detail=" task not does exist")
            
            return task
                        
            
          