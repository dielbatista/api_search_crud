from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.sql import func
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    login = Column(String(100), nullable=False, unique=True)
    hash_password = Column(String(255), nullable=False)
    active = Column(Boolean)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())