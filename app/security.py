from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha[:72])

def verificar_senha(senha_puro_texto: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_puro_texto[:72], senha_hash)
