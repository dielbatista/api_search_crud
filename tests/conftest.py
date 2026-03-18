import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db  # <--- Importe do database
from app.main import app

# URL do banco de teste
TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/api_db_test"

engine_test = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():

    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)

@pytest.fixture
def db_session():

    connection = engine_test.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(autouse=True)
def override_get_db(db_session):

    def _get_test_db():
        yield db_session
        
    app.dependency_overrides[get_db] = _get_test_db