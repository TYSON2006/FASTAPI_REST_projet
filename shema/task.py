from pydantic import BaseModel,Field

class CreateTasksValidation(BaseModel):
    title : str = Field()
    description : str = Field()
    priorities : str = Field()
    completed : bool = Field(
        default=False
    )
    
    
    
class UpdateTaskValidation(BaseModel):
    title : str|None = Field(default=None,min_length=1,max_length=100)
    description: str | None = None
    priorities:str | None = None