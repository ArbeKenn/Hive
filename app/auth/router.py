from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['Авторизация']
)

@router.post('/reg')
def registration():
    pass

@router.post('/log')
def login():
    pass

@router.post('/logout')
def logout():
    pass

@router.post('/refresh')
def refresh_token():
    pass

@router.put('/change_password')
def change_password():
    pass

@router.put('/my_profile/edit')
def edit():
    pass

@router.get('/my_profile')
def profile():
    pass