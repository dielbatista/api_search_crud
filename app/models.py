from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    login = Column(String(100), nullable=False, unique=True)
    hash_password = Column(String(255), nullable=False)
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
