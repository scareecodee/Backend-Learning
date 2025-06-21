from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"Sundram"}}

@app.get("/about")
def about():
    return {"autorDetail":{"name":"Sundram Kumar",
                           "age":18,"place":"Motihari"}}