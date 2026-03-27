from sqlalchemy.orm import Session
from . import models, security

def create_usuario(db: Session, usuario_data: dict):
    senha_plana = usuario_data.get("hash_password")
    senha_hasheada = security.gerar_hash_senha(senha_plana)
    
    novo_usuario = models.Usuario(
        name=usuario_data.get("name"),
        email=usuario_data.get("email"),
        login=usuario_data.get("login"),
        hash_password=senha_hasheada, 
        active=usuario_data.get("active", True),
        is_admin=usuario_data.get("is_admin", False) 
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def get_usuario_by_nome(db: Session, nome: str):

    return db.query(models.Usuario).filter(models.Usuario.name.ilike(f"%{nome}%")).all()

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()

def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def delete_usuario(db: Session, usuario_id: int):
    usuario = get_usuario_by_id(db, usuario_id) 
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False