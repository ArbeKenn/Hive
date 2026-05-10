from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.posts.models import Post as PostModel

router = APIRouter(
    prefix='/post',
    tags=['Publications']
)


@router.get('/posts')
def all_posts(db: Session = Depends(get_db)):
    posts = db.query(PostModel)
    return posts

@router.post('/new_post')
def create_post():
    return 'yo'