# routes/user.py

from fastapi import APIRouter, Depends
from auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/me")
def leer_usuario_actual(usuario: dict = Depends(get_current_user)):
    return usuario
