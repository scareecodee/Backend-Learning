from routers import posts , user,auth,votes
from fastapi import FastAPI



app=FastAPI()

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)