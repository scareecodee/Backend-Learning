from fastapi import FastAPI , HTTPException,status,Depends, APIRouter
from app import model ,schemas
from sqlalchemy.orm import session 
from app.database import  get_db, engine
from utils.hashing import hash_password

model.Base.metadata.create_all(bind=engine)
router=APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post('',response_model=schemas.createUserRes,status_code=status.HTTP_201_CREATED)
def createUser(user:schemas.createUserReq,db:session=Depends(get_db)):
    hashed_password=hash_password(user.password)
    user.password=hashed_password
    user=model.Users(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



@router.get("/{id}")
def getUserById(id:str,db:session=Depends(get_db)):
    user=db.query(model.users).filter(model.users.id==id).first()
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id={id} not found")