from fastapi import APIRouter
from pydantic import BaseModel
import random
from servicio_correo import enviar_correo_recuperacion
from database import connect_to_mysql, execute_query, disconnect_from_mysql

router = APIRouter()

class RecuperarRequest(BaseModel):
    email: str

def generar_codigo():
    return str(random.randint(100000, 999999))

@router.post("/recuperar")
def recuperar_password(data: RecuperarRequest):
    db = connect_to_mysql()
    query = "SELECT id FROM users WHERE email = %s"
    result = execute_query(db, query, (data.email,))
    
    if not result:
        disconnect_from_mysql(db)
        return {"message": "Si el correo existe, se enviará un código de recuperación."}

    user_id = result[0]["id"]
    codigo = generar_codigo()

    insert = "INSERT INTO password_resets (user_id, token) VALUES (%s, %s)"
    execute_query(db, insert, (user_id, codigo))
    disconnect_from_mysql(db)

    enviar_correo_recuperacion(data.email, codigo)

    return {"message": "Se ha enviado un código de recuperación al correo."}
