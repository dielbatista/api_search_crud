from app.crud import create_usuario, get_usuario_by_id, delete_usuario
from app.database import SessionLocal
from app.models import Usuario
import uuid

def gerar_email_unico():
    return f"test_{uuid.uuid4().hex[:8]}@example.com"

def test_create_usuario():
    try:
        db = SessionLocal()
        usuario_data = {
            "name": "Test User",
            "email": gerar_email_unico(),
            "login": f"login_{uuid.uuid4().hex[:8]}",
            "hash_password": "hashed_password"
        }
        usuario = create_usuario(db, usuario_data)
        
        assert usuario.id is not None
        assert usuario.name == "Test User"
        assert usuario.email == usuario_data["email"]
        assert usuario.login == usuario_data["login"]
        assert usuario.hash_password == "hashed_password"
    finally:        db.close()
    
def test_listar_usuarios():
    try:
        db = SessionLocal()
        usuarios = db.query(Usuario).all()
        assert isinstance(usuarios, list)
    finally:
        db.close()
        
def test_get_usuario_by_id():
    try:
        db = SessionLocal()
        usuario_data = {
            "name": "Test User",
            "email": gerar_email_unico(),
            "login": f"login_{uuid.uuid4().hex[:8]}",
            "hash_password": "hashed_password"
        }
        usuario = create_usuario(db, usuario_data)
        
        usuario_obtido = get_usuario_by_id(db, usuario.id)
        assert usuario_obtido is not None
        assert usuario_obtido.id == usuario.id
    finally:
        db.close()
        
def test_delete_usuario():
    try:
        db = SessionLocal()
        usuario_data = {
            "name": "Test User",
            "email": gerar_email_unico(),
            "login": f"login_{uuid.uuid4().hex[:8]}",
            "hash_password": "hashed_password"
        }
        usuario = create_usuario(db, usuario_data)
        
        resultado = delete_usuario(db, usuario.id)
        assert resultado is True
        
        usuario_obtido = get_usuario_by_id(db, usuario.id)
        assert usuario_obtido is None
    finally:
        db.close()