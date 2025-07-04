from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Post(Base):
    __tablename__="posts"

    id=Column(type_=Integer,nullable=False,primary_key=True)
    title=Column(type_=String,nullable=False)
    content=Column(type_=String,nullable=False)
    published=Column(type_=Boolean,default=True)
    created_at = Column(type_=DateTime(timezone=True), server_default=func.now()) 


# default=True: Python sets the default before sending to the DB

# server_default=func.now(): Database sets the default when inserting