from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi import APIRouter
from shema.users import  UserCreateValidation
from db.data_base import db_dependency
from services.users import  Users
from fastapi.security import OAuth2PasswordRequestForm

users_rooter = FastAPI(prefix="/users",tags=["Authentification"])



@users_rooter.post("/inscription")
async def create_user(body:UserCreateValidation, db:db_dependency):
    services = Users(db)
    return await services.create_utilisateur(body)


@users_rooter.post("/connexion") 
async def connexion(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    services = UserAuth(db)
    body = Connexion_Validation(email=form_data.username,password=form_data.password)
    return await services.connexion(body)
    
