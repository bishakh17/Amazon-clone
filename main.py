from fastapi import FastAPI
from routers import user


app = FastAPI()
app.include_router(user.router)

# @app.on_event("startup")
# async def startup():
#     await db.database.connect()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.on_event("shutdown")
# async def shutdown():
#     await db.database.disconnect()
