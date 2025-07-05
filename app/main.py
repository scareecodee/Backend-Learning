from routers import posts , user,auth
import psycopg2
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import time


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

app=FastAPI()

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)