from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import List
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    name: str
    email: EmailStr
    login: str
    active: bool = True
class LoginRequest(BaseModel):
    login: str
    password: str

class UsuarioCreate(UsuarioBase):
    hash_password: str

class Usuario(UsuarioBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # Forma correta para Pydantic V2
    model_config = ConfigDict(from_attributes=True)