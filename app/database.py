from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import dotenv 
import os
dotenv.load_dotenv()


DB_HOST = os.getenv("database_hostname")
DB_PORT = os.getenv("database_port")
DB_NAME = os.getenv("database_name")
DB_USER = os.getenv("database_username")
DB_PASSWORD = (os.getenv("database_password"))


DATABASE_URL= f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine=create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base=declarative_base()

print("🔧 DATABASE_URL =", DATABASE_URL)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
#connecting to the database using psycopg2

#         while True:
#     try:
#         conn = psycopg2.connect(
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT"),
#         cursor_factory=RealDictCursor)
#         print("Connection to DataBase was succesful")
#         break
        
#     except Exception as error:
#         print("Connection to DataBase failed")
#         print(f"error is {error}")
#         time.sleep(5)

print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)
print("DATABASE_URL:", DATABASE_URL)
