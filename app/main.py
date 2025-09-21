from fastapi import FastAPI
from app.routers import user, author

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user.router)
app.include_router(author.router)