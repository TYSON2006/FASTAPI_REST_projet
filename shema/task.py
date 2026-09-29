from pydantic import BaseModel,Field

class CreateTasksValidation(BaseModel):
    title : str = Field()
    description : str = Field()
    priorities : str = Field()
    completed : bool = Field(
        default=False
    )