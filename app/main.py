from fastapi import FastAPI
from app.routers import user, author, book, auth

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(author.router)
app.include_router(book.router)