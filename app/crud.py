from sqlalchemy.orm import Session
from . import models

def create_usuario(db: Session, usuario_data: dict):
    novo_usuario = models.Usuario(
        name=usuario_data["name"],
        email=usuario_data["email"],
        login=usuario_data["login"],
        hash_password=usuario_data["hash_password"],
        active=usuario_data.get("active", True) 
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()



def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()



def delete_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False
