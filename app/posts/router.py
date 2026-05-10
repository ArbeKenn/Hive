from fastapi import APIRouter, Depends, HTTPException
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

@router.put('/edit')
def edit_post(db: Session = Depends(get_db)):
    pass

@router.delete('/del/{post_id}')
def del_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post Not Found')
    db.delete(post)
    db.commit()
    return {'message': 'Account deleted'}