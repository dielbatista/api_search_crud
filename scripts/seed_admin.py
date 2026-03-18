from app.database import SessionLocal
from app import crud, models, security


def create_initial_admin():
    db = SessionLocal()
    try:
        admin_data = {
            "name": "Diel Admin",
            "email": "admin@sistema.com",
            "login": "admin",
            "hash_password": "jk2m53p8",
            "is_admin": True
        }

        user_exists = db.query(models.Usuario).filter(models.usuario.login == admin_data["login"]).first()
        
        if not user_exists:
            print(f"[SEED] Criando admin: {admin_data['login']}...")
            crud.create_usuario(db, admin_data)
            print("Admin Criado com Sucesso!.")
        else:
            print("[SEED] O login '{admin_data['login']}' ja Existe")
    
    except Exception as e:
        print(f"Erro no seed: {e}")
    finally:
        db.close()
        
if __name__ == "__main__":
    create_initial_admin()