from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from utils.hashing import hash_password,verify_password
from utils.outh2 import jwtTokenGenerator
from app import model , schemas
from app.database import engine,get_db
from jose import JWTError,jwt


model.Base.metadata.create_all(bind=engine)


SECRET_KEY="3ufjq39djf8j@93jf0sjdlajfJFSJAKfnnl493jjn293hf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router=APIRouter()

# {"username":"heyy", "password":"12345}" ----> OAuth2PasswordRequestForm

@router.post("/login",response_model=schemas.Token)
def login(credential:OAuth2PasswordRequestForm=Depends(),db=Depends(get_db)):
    user=db.query(model.users).filter(model.users.
    email==credential.username).first()
    if user:
        pass_entered=credential.password
        hash_storedInDB=user.password
        if verify_password(pass_entered,hash_storedInDB):
            print(user.id)
            token=jwtTokenGenerator({"user_id":user.id})
            return {"access_token":token,"token_type":"bearer"}
        return "wrong credential"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="No user found")
    




