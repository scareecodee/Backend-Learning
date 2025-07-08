from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="posts"

    id=Column(type_=Integer,nullable=False,primary_key=True)
    title=Column(type_=String,nullable=False)
    content=Column(type_=String,nullable=False)
    published=Column(type_=Boolean,default=True)
    created_at = Column(type_=DateTime(timezone=True), server_default=func.now()) 
    owner_id=Column(String,ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    owner=relationship("Users")


# default=True: Python sets the default before sending to the DB

# server_default=func.now(): Database sets the default when inserting

# for registration
class Users(Base):
    __tablename__="users"
    id=Column(type_=String,primary_key=True,nullable=False)
    email=Column(type_=String,nullable=False,unique=True)
    password=Column(type_=String,nullable=False)
    created_at = Column(type_=DateTime(timezone=True), server_default=func.now()) 

#for votes/likes
class Vote(Base):
    __tablename__="votes"

    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    user_id=Column( String,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True,nullable=False)
