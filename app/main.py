from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import create_tables, get_db
from app.user.router import router as user_router
from app.posts.router import router as post_router
from app.posts.models import Post as PostModel


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
def home(db: Session = Depends(get_db)):
    posts = db.query(PostModel).order_by(PostModel.id.desc()).limit(10).all()
    return {
        'latest_posts': posts,
    }
