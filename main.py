from fastapi import FastAPI, Depends
from utils import db

app = FastAPI()
db.create_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

