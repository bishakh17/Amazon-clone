from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/signup")
async def signup(user: User):
    for name in users:
        if name.username == user.username:
            return {"message": "User Already Exists"}
    users.append(user)
    return user

@app.get("/login")
async def login(username: str, password: str):
    for user in users:
        if user.username == username and user.password == password:
            return {"message": "Login Successful"}
    return {"message": "Login Failed"}
