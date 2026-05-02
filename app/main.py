from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from auth.router import router as auth_router

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


app.include_router(auth_router)

@app.get('/')
def home():
    return {
        'message': 'Добро пожаловать в API! Перейдите на /docs для документации.'
    }
