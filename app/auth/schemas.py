from pydantic import BaseModel
class UserSchema(BaseModel):
    username : str
    password: str
    email: str | None
    phone: str
    age: int
    gender: str

class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str | None
    phone: str
    age: int
    gender: str

    class Config:
        from_attribute = True