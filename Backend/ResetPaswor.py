from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import connect_to_mysql, execute_query, disconnect_from_mysql
import bcrypt

router = APIRouter()

class ResetInput(BaseModel):
    codigo: str
    nueva_password: str

@router.post("/reset")
def reset_password(data: ResetInput):
    db = connect_to_mysql()
    token_data = execute_query(db, "SELECT user_id FROM password_resets WHERE token = %s", (data.codigo,))
    
    if not token_data:
        disconnect_from_mysql(db)
        raise HTTPException(status_code=400, detail="Código inválido o expirado")

    user_id = token_data[0]["user_id"]
    hashed_pw = bcrypt.hashpw(data.nueva_password.encode(), bcrypt.gensalt()).decode()

    execute_query(db, "UPDATE users SET password = %s WHERE id = %s", (hashed_pw, user_id))
    #execute_query(db, "DELETE FROM password_resets WHERE token = %s", (data.codigo,))

    disconnect_from_mysql(db)
    return {"message": "Contraseña actualizada correctamente"}
