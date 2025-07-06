from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "udddgbjow2ox92kjkqjk99mksxjjijwikkjsggd7204sbcyff"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def jwtTokenGenerator(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire.timestamp()})
    jwtToken=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return jwtToken

