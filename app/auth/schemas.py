from pydantic import BaseModel
class User(BaseModel):
    username : str
    password: str
    email: str | None
    phone: str
    age: int
    gender: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    age: int
    gender: str
    is_staff: bool = False

    class Config:
        from_attribute = True