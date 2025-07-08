from fastapi import FastAPI , HTTPException,status,Depends, APIRouter
from app import model ,schemas
from sqlalchemy.orm import session 
from app.database import  get_db, engine
from utils.outh2 import getCurrentUser


model.Base.metadata.create_all(bind=engine)

router=APIRouter(
    prefix="/vote",
    tags=['votes']
)

@router.post('',response_model=schemas.VoteRes)
def votingSystem(VoteReq:schemas.VoteReq,db:session=Depends(get_db),user_id:int=Depends(getCurrentUser)):
    post_query=db.query(model.Post).filter(model.Post.id==VoteReq.post_id).first()
    if post_query is None:
        print("post not in db")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    vote_casted=db.query(model.Vote).filter(VoteReq.post_id==model.Vote.post_id,user_id==model.Vote.user_id).first()
    if VoteReq.vote_direction==1:
        if vote_casted is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        new_vote = model.Vote(post_id=VoteReq.post_id, user_id=user_id)
        db.add(new_vote)
        db.commit()
        return schemas.VoteRes(
          post_id=VoteReq.post_id,
          user_id=user_id,
          vote_direction=VoteReq.vote_direction
        )
    else:
        if vote_casted is not None:
            db.delete(vote_casted)
            db.commit()
            return schemas.VoteRes(
            post_id=VoteReq.post_id,
             user_id=user_id,
            vote_direction=VoteReq.vote_direction
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
   
    

