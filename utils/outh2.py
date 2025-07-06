from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from app import model 
from app.database import get_db
from app.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# This line defines how FastAPI should extract the JWT token from the incoming HTTP request.
# OAuth2PasswordBearer – What Is It?
# It’s a class provided by FastAPI that:
# Looks for the Authorization header.
# Verifies that it starts with Bearer .
# Extracts the token after Bearer .
# Returns that token as a str.

SECRET_KEY="3ufjq39djf8j@93jf0sjdlajfJFSJAKfnnl493jjn293hf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def jwtTokenGenerator(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":int(expire.timestamp())})
    jwtToken=jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return jwtToken


def verifyJwtToken(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"})
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=TokenData(id=id)
        return token_data
    except JWTError:
        raise credentials_exception
            
def getCurrentUser(token:str=Depends(oauth2_scheme),db=Depends(get_db)):
    return verifyJwtToken(token,db)
      
