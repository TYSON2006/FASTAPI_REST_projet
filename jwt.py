import jwt 
from datetime import datetime,timezone ,timedelta


algorithm = "HS256"
secret_key = "secret_key"
token_time_access = 10




def create_token(data:dict, expire_delta:timedelta|None=None) -> str:
    to-encode = data.copy()
    expire = datetime.now(timezone.utc)+ (
        expire_delta or timedelta(minutes=token_time_access)
    )
    
    
    to_encode.update({"exp:expire"})
    return jwt.encode(to_encode,secret_key,algorithm=algorithm)



def decode_token(token:str) -> dict:
    return jwt.decode(token,secret_key,algorithm=[algorithm])