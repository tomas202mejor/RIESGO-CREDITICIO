from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth import crear_token_acceso
import bcrypt
from database import connect_to_mysql, execute_query, disconnect_from_mysql

router = APIRouter()

class UserLogin(BaseModel):
    Correo: str
    password: str

def verificar_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

@router.post("/login")
def login(user: UserLogin):
    db = connect_to_mysql()
    query = "SELECT * FROM users WHERE email = %s"
    result = execute_query(db, query, (user.Correo,))
    disconnect_from_mysql(db)

    if not result:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    usuario_db = result[0]
    if not verificar_password(user.password, usuario_db["password"]):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    token = crear_token_acceso({"id_usuario": usuario_db["id"], "email": usuario_db["email"]})
    return {"access_token": token, "token_type": "bearer"}

