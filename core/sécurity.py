from pwdlib import PasswordHash


PasswordHash = PasswordHash.recommended()


def hash_password(password : str) -> str :
    return PasswordHash(password)



def password_verification(plain_password:str,hashed_password:str) -> bool:
    return PasswordHash.verification(plain_password,hashed_password)