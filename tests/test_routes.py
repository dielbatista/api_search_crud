import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Função auxiliar para gerar dados únicos e não dar erro de banco
def random_user_data():
    uid = uuid.uuid4().hex[:6]
    return {
        "name": f"User {uid}",
        "email": f"{uid}@test.com",
        "login": f"login_{uid}",
        "hash_password": "123"
    }

def test_read_usuario_not_found():
    """Testa se buscar um ID inexistente retorna 404"""
    response = client.get("/usuarios/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario not found"

def test_fluxo_completo_usuario():
    """Testa o fluxo completo: criar, ler, deletar e verificar exclusão"""
    # 1. CRIAR (POST)
    payload = random_user_data()
    post_response = client.post("/usuarios", json=payload)
    assert post_response.status_code == 200
    user_id = post_response.json()["id"]

    # 2. LER (GET)
    get_response = client.get(f"/usuarios/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["login"] == payload["login"]

    # 3. DELETAR (DELETE)
    del_response = client.delete(f"/usuarios/{user_id}")
    assert del_response.status_code == 200
    assert del_response.json()["message"] == "Usuario deleted successfully"

    # 4. VERIFICAR (GET final deve ser 404)
    final_get = client.get(f"/usuarios/{user_id}")
    assert final_get.status_code == 404

def test_delete_usuario_not_found():
    """Testa se deletar um ID inexistente retorna 404"""
    response = client.delete("/usuarios/999999")
    assert response.status_code == 404