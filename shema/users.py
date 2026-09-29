from pydantic import BaseModel, EmailStr ,Field
from datetime import datetime


class UserCreateValidation(BaseModel):
    name : str = Field(min_length=3,max_length=50)
    last_name : str = Field(min_length=3,max_length=50)
    email : EmailStr = Field (min_length=3,max_length=50)
    password :  str = Field(min_length=10)
        
        

class UserLogin(BaseModel):
    email : EmailStr
    password : str  
    


class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    date_creation : datetime


    class Config :
         from_attributes = True

