from app.models import Usuario

def test_usuario_table_name():
    assert Usuario.__tablename__ == "usuarios"