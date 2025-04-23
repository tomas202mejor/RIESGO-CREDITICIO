from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dbConnection import connect_to_mysql, execute_query, disconnect_from_mysql
from dotenv import load_dotenv
import os
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configura logging (esto es mejor que usar print cuando estás en producción o debug más fino)
logging.basicConfig(level=logging.INFO)

# Cargar variables del entorno
load_dotenv(dotenv_path='.venv/.env')

app = FastAPI()

# Agregar el middleware CORS
origins = [
    "http://localhost:3000",  # Aquí pones el origen de tu frontend (puede ser localhost o el dominio correspondiente)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class UserLogin(BaseModel):
    Correo: str
    password: str

def transformarClave(clave: str) -> str:
    clave_c = clave.upper()
    clave_bin = ''.join(format(ord(c), '08b') for c in clave_c)
    logging.info(f"Clave original: {clave} | Clave transformada: {clave_bin}")
    return clave_bin

@app.post("/login")
def login(user: UserLogin):
    logging.info(f" Petición recibida con correo: {user.Correo}")

    claveTransformada = transformarClave(user.password)

    db_connection = connect_to_mysql(
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_DATABASE')
    )
    
    if not db_connection:
        logging.error(" Fallo la conexión a la base de datos.")
        raise HTTPException(status_code=500, detail="No se pudo conectar a la base de datos")
    
    query = "SELECT * FROM usuario WHERE Correo = %s AND clave = %s"
    logging.info(f"📄 Ejecutando consulta: {query} con valores: ({user.Correo}, {claveTransformada})")

    result = execute_query(db_connection, query, (user.Correo, claveTransformada))
    
    disconnect_from_mysql(db_connection)

    if result:
        logging.info(" Usuario autenticado correctamente.")
    else:
        logging.warning(" Usuario o contraseña incorrectos.")

    return {"ok": result is not None}
