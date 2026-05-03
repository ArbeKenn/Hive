from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.auth.schemas import UserSchema, UserLoginSchema, UserResponseSchema
from app.auth.models import User as UserModel
from app.database import SessionLocal, get_db

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация']
)
#I connect the JWT token tomorrow.

#temporarily to check which users are in the database
@router.get('/all')
def all_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@router.post('/reg')
def registration(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/log', response_model=UserLoginSchema)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(
        UserModel.username == user.username,
        UserModel.password == user.password
    ).first()
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail='Incorrect login or password'
        )
    return user

@router.post('/refresh')
def refresh_token():
    pass

@router.put('/change_password')
def change_password():
    pass

@router.get('/my_profile', response_model=UserResponseSchema)
def profile(db: Session = Depends(get_db)):
    user_profile = db.query(UserModel).first()
    return user_profile

@router.put('/my_profile/edit/{user_id}', response_model=UserResponseSchema)
def edit_profile(user_id: int, user: UserResponseSchema, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail='Пользователь не найден')

    for key, value in user.model_dump().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete('/my_profile/del/{user_id}')
def del_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User Not Found')
    db.delete(user)
    db.commit()
    return {'message': 'Account deleted'}