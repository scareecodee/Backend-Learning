from pydantic import BaseModel, EmailStr
from typing import Optional

#creating schema for creating post or retreving post
class Post(BaseModel):
    title:str
    content:str
    published:bool

#creating req schema for registration of user

class createUserReq(BaseModel):
    id:str
    email:EmailStr
    password:str

#creating response schema for registration of user
class createUserRes(BaseModel):
    id:str
    email:EmailStr
    class Config:
        from_attributes = True

#creating schema for response
class res(BaseModel):
    title:str
    content:str
    published:bool
    owner:createUserRes
    class Config:
        from_attributes = True



    
#login req
class loginReqSchema(BaseModel):
    password:str
    email:EmailStr

# login response schema
class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        from_attributes = True

class TokenData(BaseModel):  #data to be embeded in payload of jwt token
    id:Optional[str]= None
