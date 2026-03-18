import uuid
import pytest
from app import crud, security
from app.models import Usuario

def gerar_dados_teste(is_admin=False):
    """Função auxiliar para gerar dados únicos e evitar repetição"""
    random_id = uuid.uuid4().hex[:8]
    return {
        "name": f"Diel Batista {random_id}",
        "email": f"test_{random_id}@example.com",
        "login": f"login_{random_id}",
        "hash_password": "minha_senha_123",
        "is_admin": is_admin
    }

def test_create_usuario(db_session):
    senha_plana = "minha_senha_123"
    usuario_data = gerar_dados_teste()

    usuario = crud.create_usuario(db_session, usuario_data)
    
    assert usuario.id is not None
    # Garante que a senha no banco NÃO é a senha plana
    assert usuario.hash_password != senha_plana
    # Garante que o "desbloqueio" (verificação) funciona
    assert security.verificar_senha(senha_plana, usuario.hash_password) is True

def test_create_admin(db_session):
    admin_data = gerar_dados_teste(is_admin=True)
    usuario = crud.create_usuario(db_session, admin_data)
    
    assert usuario.is_admin is True
    assert usuario.name.startswith("Diel Batista")

def test_listar_usuarios(db_session):
    # Usando db_session garantimos que estamos no banco de teste isolado
    usuarios = crud.listar_usuarios(db_session)
    assert isinstance(usuarios, list)

def test_get_usuario_by_nome(db_session):
    usuario_data = gerar_dados_teste()
    usuario_data["name"] = "Diel Batista Específico"
    
    crud.create_usuario(db_session, usuario_data)
    resultado = crud.get_usuario_by_nome(db_session, "Específico")
    
    assert len(resultado) > 0
    assert "Específico" in resultado[0].name

def test_get_usuario_by_id(db_session):
    usuario_data = gerar_dados_teste()
    usuario = crud.create_usuario(db_session, usuario_data)
    
    usuario_obtido = crud.get_usuario_by_id(db_session, usuario.id)
    assert usuario_obtido is not None
    assert usuario_obtido.id == usuario.id

def test_delete_usuario(db_session):
    usuario_data = gerar_dados_teste()
    usuario = crud.create_usuario(db_session, usuario_data)
    
    resultado = crud.delete_usuario(db_session, usuario.id)
    assert resultado is True
    
    usuario_obtido = crud.get_usuario_by_id(db_session, usuario.id)
    assert usuario_obtido is None