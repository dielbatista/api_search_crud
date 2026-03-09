import pytest
from app.database import Base, engine, SessionLocal
from app.models import Usuario

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """
    Garante que as tabelas existam antes de iniciar qualquer teste.
    O 'scope=session' faz isso rodar apenas UMA vez por bateria de testes.
    """
    # Cria as tabelas (caso tenham sido apagadas pelo DROP)
    Base.metadata.create_all(bind=engine)
    
    yield  # Aqui o pytest executa os testes
    
    # Opcional: Se quiser limpar tudo após os testes, descomente a linha abaixo:
    # Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    """
    Fixture para fornecer uma sessão de banco de dados limpa para cada teste.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()