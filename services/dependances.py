from fastapi.security import OAuth2PasswordBearer 
from fastapi import Depends,HTTPException,status
import jwt 
from typing import Annotated
from jwt import decode_token
from db.data_base import db_dependency
from models._models_users import Users
from sqlalchemy import select



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/connexion")


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)],db:db_dependency) -> Users:
    credentials_errors  = HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token access failed",
        
        
    )
    
    
    try : 
        playload = decode_token(token)
        user_id = playload.getif ("sub")
        if user_id is None :
            raise credentials_errors
    except jwt.InvalidTokenError:
        raise credentials_errors
    
    
    result = await db.execute(select(Users).where(Users.id ==int(user_id)))
    user = result.scalar_one_or_none()
    if user is None:
        raise credentials_errors
    return user