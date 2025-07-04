from fastapi import FastAPI , Response, HTTPException,status,Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import cursor 
from dotenv import load_dotenv
import os
import time
from . import model
from sqlalchemy.orm import session 
from .database import engine, get_db


model.Base.metadata.create_all(bind=engine)


app=FastAPI()


while True:
    try:
        conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        cursor_factory=RealDictCursor)
        print("Connection to DataBase was succesful")
        break
        
    except Exception as error:
        print("Connection to DataBase failed")
        print(f"error is {error}")
        time.sleep(5)



@app.get("/")
def root():
    return {"data":"Server is Running..."}

@app.get("/posts")
def getAllPosts():
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM posts''')
    posts=cursor.fetchall()
    print(posts)
    return {"data":posts}


@app.get('/sqlalchemy')
def test_post(db:session=Depends(get_db)):
    return {"data":"Succesful created table"}



#creating schema
class Post(BaseModel):
    title:str
    content:str
    published:bool
 

@app.post("/post")
def createPost(post:Post,response:Response):
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *;''',
                   (post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    print(new_post)
    return {"data":"post created"}

@app.get("/post/{id}")
def getPostById(id:int,response:Response):
    cursor=conn.cursor()
    cursor.execute('''SELECT * from posts WHERE id=(%s) ''',(id,))
    post=cursor.fetchone()
    if post:
        print(post)
        return {"details":post}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with id {id} not found"}



@app.delete("/post/{id}")
def deletePost(id:int,response:Response):
    cursor=conn.cursor()
    cursor.execute('DELETE from posts WHERE id=(%s) RETURNING *;',(id,))
    deleted_post=cursor.fetchone()
    if deleted_post is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with id {id} not found"}

    return {"message": "Post deleted", "data": deleted_post}


@app.put("/post/{id}")
def updatePost(id:int,post:Post):
    cursor=conn.cursor()
    cursor.execute(
        '''
        UPDATE posts
        SET title = %s, content = %s, published = %s
        WHERE id = %s
        RETURNING *;
        ''',
        (post.title, post.content, post.published, id)
    )
    updated_post=cursor.fetchone()
    conn.commit()
    if updated_post:
        return {"message":"post updated", "details":updated_post}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
                            f'post with id={id} not found')


