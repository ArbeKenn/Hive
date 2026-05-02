from sqlalchemy import Column, String, Integer, Boolean, DateTime, func
from app.database import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    is_staff = Column(Boolean, default=False)
    age = Column(Integer)
    gender = Column(String)
    date_joined = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)
