from fastapi import APIRouter, Depends
from typing import Annotated
from shema.users import  UserCreateValidation , UserLogin
from db.data_base import db_dependency
from services.users import  Users , UsersService
from fastapi.security import OAuth2PasswordRequestForm

users_router = APIRouter(prefix="/users",tags=["Authentification"])



@users_router.post("/inscription")
async def create_user(body:UserCreateValidation, db:db_dependency):
    services = Users(db)
    return await services.create_utilisateur(body)


@users_router.post("/connexion") 
async def connexion(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    services = Users(db)
    body = UsersService(email=form_data.username,password=form_data.password)
    return await services.connexion(body)
    
