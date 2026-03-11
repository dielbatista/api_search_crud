from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()


@router.post("/usuarios")
def create_usuario(usuario_data: dict, db: Session = Depends(get_db)):
    return crud.create_usuario(db, usuario_data)    


@router.get("/usuarios/{usuario_id}")
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_id(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@router.get("/usuarios/busca")
def search_usuarios(nome: str, db: Session = Depends(get_db)):
    usuarios = crud.get_usuario_by_nome(db, nome)
    return usuarios

@router.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario_by_id(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    crud.delete_usuario(db, usuario_id)
    return {"message": "Usuario deleted successfully"}