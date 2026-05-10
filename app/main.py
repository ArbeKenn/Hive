from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables
from app.user.router import router as user_router
from app.posts.router import router as post_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title='Hive',
    description='API for school',
    version='0.1.0',
    lifespan=lifespan,
)


app.include_router(user_router)
app.include_router(post_router)

@app.get('/')
def home():
    return {
        'message': 'Добро пожаловать в API! Перейдите на /docs для документации.'
    }
