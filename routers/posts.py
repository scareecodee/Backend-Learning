from fastapi import FastAPI , Response, HTTPException,status,Depends,APIRouter
import psycopg2
from typing import List
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import time
from app import model ,schemas
from sqlalchemy.orm import session 
from app.database import engine, get_db

#"Look at all classes that inherit from Base (your SQLAlchemy models), and create the corresponding tables in the database — if they don’t already exist."
model.Base.metadata.create_all(bind=engine)


router=APIRouter(
    prefix="/post",
    tags=['posts']
)


# @app.get("/posts")
# def getAllPosts():
#     cursor=conn.cursor()
#     cursor.execute('''SELECT * FROM posts''')
#     posts=cursor.fetchall()
#     print(posts)
#     return {"data":posts}


#  ----------------OR--------------------------

@router.get('',response_model=List[schemas.res])
def test_post(db:session=Depends(get_db)):
    posts=db.query(model.Post).all()
    return posts




 

# @app.post("/post")
# def createPost(post:Post,response:Response):
#     cursor=conn.cursor()
#     cursor.execute('''INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *;''',
#                    (post.title,post.content,post.published))
#     new_post=cursor.fetchone()
#     conn.commit()
#     print(new_post)
#     return {"data":"post created"}

# -------------------OR----------------------------------

@router.post('',response_model=schemas.res)
def createPost(post:schemas.Post,db:session=Depends(get_db)):
    new_post=model.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @app.get("/post/{id}")
# def getPostById(id:int,response:Response):
#     cursor=conn.cursor()
#     cursor.execute('''SELECT * from posts WHERE id=(%s) ''',(id,))
#     post=cursor.fetchone()
#     if post:
#         print(post)
#         return {"details":post}
#     else:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"error": f"Post with id {id} not found"}


# ------------------------OR----------------------

@router.get("/{id}",response_model=schemas.res)
def getPostById(id:int,db:session=Depends(get_db)):
    post=db.query(model.Post).filter(model.Post.id==id).first()
    if post:
        print(type(post))
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with is {id} not found")




# @app.delete("/post/{id}")
# def deletePost(id:int,response:Response):
#     cursor=conn.cursor()
#     cursor.execute('DELETE from posts WHERE id=(%s) RETURNING *;',(id,))
#     deleted_post=cursor.fetchone()
#     if deleted_post is None:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"error": f"Post with id {id} not found"}

#     return {"message": "Post deleted", "data": deleted_post}


# -------------------OR--------------------------

@router.delete("/{id}",response_model=schemas.res)
def deletePost(id:int,db:session=Depends(get_db)):
    deleted_post=db.query(model.Post).filter(model.Post.id==id).first()
    if deleted_post:
        db.delete(deleted_post)
        db.commit()
        return deleted_post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with is {id} not found")
          



# @app.put("/post/{id}")
# def updatePost(id:int,post:Post):
#     cursor=conn.cursor()
#     cursor.execute(
#         '''
#         UPDATE posts
#         SET title = %s, content = %s, published = %s
#         WHERE id = %s
#         RETURNING *;
#         ''',
#         (post.title, post.content, post.published, id)
#     )
#     updated_post=cursor.fetchone()
#     conn.commit()
#     if updated_post:
#         return {"message":"post updated", "details":updated_post}
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=
#                             f'post with id={id} not found')


#------------------------OR----------------------------------------------



@router.put("/{id}",response_model=schemas.res)
def update_post(response: Response, id: int, post: schemas.Post, db:session = Depends(get_db)):
    post_query = db.query(model.Post).filter(model.Post.id == id)

    existing_post = post_query.first()
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with is {id} not found")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(existing_post) 

    return  existing_post