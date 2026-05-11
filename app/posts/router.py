from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.posts.models import Post as PostModel
from app.posts.schemas import PostCreateUpdateSchema
from app.user.jwt import get_current_user

router = APIRouter(
    prefix='/post',
    tags=['Publications']
)


@router.get('/posts')
def all_posts(db: Session = Depends(get_db)):
    posts = db.query(PostModel).all()
    return posts

@router.post('/new_post')
def create_post(
        post: PostCreateUpdateSchema,
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):

    new_post = PostModel(**post.model_dump())
    new_post.user_id = user_id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.put('/edit/{post_id}')
def edit_post(
        post_id: int,
        post_schema: PostCreateUpdateSchema,
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):

    post = db.query(PostModel).filter(
        PostModel.id == post_id
    ).first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail='Post Not Found')

    for key, value in post_schema.model_dump().items():
        setattr(post, key, value)

    post.user_id = user_id
    db.commit()
    db.refresh(post)
    return post

@router.delete('/del/{post_id}')
def del_post(
        post_id: int,
        db: Session = Depends(get_db),
        user_id: int = Depends(get_current_user)
):

    post = db.query(PostModel).filter(
        PostModel.id == post_id
    ).first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail='Post Not Found')

    if post.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail='Not your post'
        )

    db.delete(post)
    db.commit()
    return {'message': 'Post deleted'}