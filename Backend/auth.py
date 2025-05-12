from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path='.venv/.env')

SECRET_KEY = os.getenv("SECRET_KEY", "secreto123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Función para crear el token JWT
def crear_token_acceso(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Función para verificar y decodificar el token JWT
def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Puedes agregar más validaciones aquí si lo necesitas (por ejemplo, verificar si el correo existe)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

# Dependencia que extrae los datos del usuario desde el token
def obtener_usuario_desde_token(token: str = Depends(oauth2_scheme)):
    # Decodificamos el token para obtener el usuario
    payload = verificar_token(token)
    # Extraemos la información del usuario (ID y email) del payload
    email: str = payload.get("email")
    id_usuario: int = payload.get("id_usuario")
    if not email or not id_usuario:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    # Retornamos los datos del usuario (esto será útil para hacer consultas a la base de datos)
    return {"email": email, "id_usuario": id_usuario}

# Esta función es un alias para obtener el usuario actual desde el token
get_current_user = obtener_usuario_desde_token
