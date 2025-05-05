from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dbConnection import connect_to_mysql, execute_query, disconnect_from_mysql
from dotenv import load_dotenv
import os
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno
load_dotenv(dotenv_path='.venv/.env')

router = APIRouter()

class UserLogin(BaseModel):
    Correo: str
    password: str

def transformarpassword(password: str) -> str:
    password_c = password.upper()
    password_bin = ''.join(format(ord(c), '08b') for c in password_c)
    logging.info(f"password original: {password} | password transformada: {password_bin}")
    return password_bin

@router.post("/login")
def login(user: UserLogin):
    logging.info(f"Petición recibida con correo: {user.Correo}")

    passwordTransformada = transformarpassword(user.password)

    # ✅ Llamamos a la función sin pasar argumentos
    db_connection = connect_to_mysql()

    if not db_connection:
        logging.error("Falló la conexión a la base de datos.")
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos")

    query = "SELECT * FROM usuario WHERE Correo = %s AND password = %s"
    logging.info(f"📄 Ejecutando consulta: {query} con valores: ({user.Correo}, {passwordTransformada})")

    result = execute_query(db_connection, query, (user.Correo, passwordTransformada))

    disconnect_from_mysql(db_connection)

    if result:
        logging.info("✅ Usuario autenticado correctamente.")
        return {"ok": True}
    else:
        logging.warning("⚠️ Usuario o contraseña incorrectos.")
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
