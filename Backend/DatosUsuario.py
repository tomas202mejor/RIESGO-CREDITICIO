from fastapi import APIRouter, Depends, HTTPException
from schemas import UserResponse
from auth import get_current_user
from database import connect_to_mysql, execute_query, disconnect_from_mysql

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_user_data(current_user: dict = Depends(get_current_user)):
    db = None
    try:
        db = connect_to_mysql()
        query = "SELECT * FROM users WHERE email = %s"
        result = execute_query(db, query, (current_user["email"],))  

        if not result:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        usuario_db = result[0]

        usuario_respuesta = {
            "id": usuario_db.get("id"),
            "username": usuario_db.get("Nusuario"),
            "email": usuario_db.get("email"),
            "nombre": f'{usuario_db.get("nombre", "")} {usuario_db.get("apellido", "")}',
            "telefono": usuario_db.get("telefono"),
            "Ndocumento": usuario_db.get("Ndocumento")
        }

        return usuario_respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

    finally:
        disconnect_from_mysql(db)
