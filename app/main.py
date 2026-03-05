from fastapi import FastAPI
from app.routes import router as usuario_router
from app.database import Base, engine

app = FastAPI()
app.include_router(usuario_router)

@app.get("/")
def root():
    return {"message": "API funcionando"}