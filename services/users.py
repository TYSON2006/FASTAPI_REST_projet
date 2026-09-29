from shema.users import UserLogin,UserCreateValidation
from models._models_users import Users
from db.data_base import db_dependency
from fastapi import HTTPException,status
from loguru import logger
from sqlalchemy import select 
from pwdlib import PasswordHash


pwd_context = PasswordHash.recommended() 


class UsersService:
    def __init__(self,db:db_dependency):
        self.db = db
   
    async def inscription(self,body_user:UserCreateValidation):
        result = await self.db.execute(select(Users).where(Users.email==body_user.email))
        
        utlisation_exite= result.scalar_one_or_none()
        if utlisation_exite:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="please try again")
        
        password_hash = pwd_context.hash(body_user.password)
        
        
        nouvel_utilisateur = Users(
            name = body_user.name,
            last_name = body_user.last_name,
            email = body_user.email,
            password = password_hash
            
            
            
        )
        
        self.db.add(nouvel_utilisateur)
        await  self.db.commit()
        await self.db.refresh(nouvel_utilisateur)
        logger.info("user insert successfully")
        return nouvel_utilisateur
    
    
    async def connexion(self,user:connexion):
        result = await self.db.execute(
            select(Users).where(Users, email ==user.email)
            
        )
        Users_db = result.scalar_one_or_none()
        print(Users_db)
        if not Users_db or not pwd_context.verify(
            user.password,
            Users_db.password
        ):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="password not found please try again")
            
            
        token_access = create_token ({"sub : str(users_db.id)"})
        return{"access_token":token_access}
        


    
       