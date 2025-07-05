from pydantic import BaseModel, EmailStr

#creating schema for creating post or retreving post
class Post(BaseModel):
    title:str
    content:str
    published:bool

#creating schema for response

class res(BaseModel):
    title:str
    content:str
    published:bool
    class Config:
        from_attributes = True


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