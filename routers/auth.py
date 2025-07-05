from fastapi import APIRouter,Depends,HTTPException,status
from utils.hashing import hash_password,verify_password
from app.schemas import loginReqSchema
from app import model 
from app.database import engine,get_db

model.Base.metadata.create_all(bind=engine)
router=APIRouter()

@router.get("/login")
def login(credential:loginReqSchema,db=Depends(get_db)):
    user=db.query(model.users).filter(model.users.
    email==credential.email).first()
    if user:
        pass_entered=credential.password
        hash_storedInDB=user.password
        if verify_password(pass_entered,hash_storedInDB):
            return "login succesfull"
        return "wrong credential"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="No user found")
    



