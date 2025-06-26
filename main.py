from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app=FastAPI()





@app.get("/")
def root():
    return {"data":"Root Path"}

@app.get("/about")
def root():
    return {"data":{
        "name":"Sundram",
        "age":18,
        "Gender":"Male"
    }}


#creating schema
class Post(BaseModel):
    title:str
    post_no:int
    published:bool
    rating:Optional[int]=None



@app.post("/createpost")
def createpost(new_post:Post):
    print(new_post)
    return {"data":f"The title of post is {new_post.title} and the post no. is {new_post.post_no} and post status is {new_post.published}"}