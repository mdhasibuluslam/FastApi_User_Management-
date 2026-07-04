from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.core.config import settings 

def create_access_token(subject:str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    playload = {
        "sub":subject,
        "exp":expire,
        "type":"access"

    }
    return jwt.encode(playload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

def decode_token(token:str):
    try:
        return jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    except:
        return None
    
    