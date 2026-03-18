import pytest
from app.security import gerar_hash_senha, verificar_senha

def test_gerar_hash_senha():
    senha_plana = "senha_curta"
    hash_gerado = gerar_hash_senha(senha_plana)
    assert hash_gerado != senha_plana
    
    assert hash_gerado.startswith("$2b$")

def test_verificar_senha_correta():
    senha_plana = "123456"
    hash_gerado = gerar_hash_senha(senha_plana)

    assert verificar_senha(senha_plana, hash_gerado) is True

def test_verificar_senha_incorreta():
    senha_plana = "123456"
    senha_errada = "654321"
    hash_gerado = gerar_hash_senha(senha_plana)
    
    # Deve retornar False para a senha errada
    assert verificar_senha(senha_errada, hash_gerado) is False

def test_hashes_diferentes_para_mesma_senha():
    senha = "senha_igual"
    hash1 = gerar_hash_senha(senha)
    hash2 = gerar_hash_senha(senha)
    
    # O bcrypt usa um "salt" aleatório, então dois hashes 
    # da mesma senha devem ser diferentes entre si.
    assert hash1 != hash2