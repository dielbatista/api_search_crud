from app import security

def test_login_sucesso(db_session):
    senha_plana = "senha123"
    hash_db = security.gerar_hash_senha(senha_plana)
    
    assert security.verificar_senha(senha_plana, hash_db) is True

def test_login_senha_errada(db_session):
    senha_real = "senha123"
    senha_tentada = "senha_errada"
    hash_db = security.gerar_hash_senha(senha_real)
    
    assert security.verificar_senha(senha_tentada, hash_db) is False
    