from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from dbConnection import connect_to_mysql, execute_query, disconnect_from_mysql
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

# Cargar variables de entorno
load_dotenv(dotenv_path='.venv/.env')

# Configurar logging
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Microservicio de Registro de Usuario")

# Configurar CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegister(BaseModel):
    nombre: str
    apellido: str
    Nusuario: str
    Ndocumento: str
    email: str
    telefono: str
    password: str

def transformarClave(clave: str) -> str:
    clave_c = clave.upper()
    clave_bin = ''.join(format(ord(c), '08b') for c in clave_c)
    logging.info(f"Clave transformada: {clave_bin}")
    return clave_bin

@app.post("/registro")
def registrar_usuario(user: UserRegister):
    db_connection = connect_to_mysql(
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_DATABASE')
    )

    if not db_connection:
        logging.error("❌ No se pudo conectar a la base de datos")
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    # Validar que los datos no estén duplicados utilizando execute_query
    try:
        # Revisar si ya existe el Nusuario
        query = "SELECT 1 FROM usuario WHERE Nusuario = %s"
        result = execute_query(db_connection, query, (user.Nusuario,))
        if result and len(result) > 0:
            return {"ok": False, "mensaje": "El usuario ya está registrado"}

        # Revisar si ya existe el Ndocumento
        query = "SELECT 1 FROM usuario WHERE Ndocumento = %s"
        result = execute_query(db_connection, query, (user.Ndocumento,))
        if result and len(result) > 0:
            return {"ok": False, "mensaje": "El documento ya está registrado"}

        # Revisar si ya existe el email
        query = "SELECT 1 FROM usuario WHERE correo = %s"
        result = execute_query(db_connection, query, (user.email,))
        if result and len(result) > 0:
            return {"ok": False, "mensaje": "El correo ya está registrado"}

        # Revisar si ya existe el teléfono
        query = "SELECT 1 FROM usuario WHERE telefono = %s"
        result = execute_query(db_connection, query, (user.telefono,))
        if result and len(result) > 0:
            return {"ok": False, "mensaje": "El teléfono ya está registrado"}
        
    except Exception as e:
        logging.error(f"❌ Error al validar los datos: {e}")
        return {"ok": False, "mensaje": "Error al validar los datos"}

    # Si pasa las validaciones, se inserta en la base de datos
    clave_transformada = transformarClave(user.password)

    insert_query = """
        INSERT INTO usuario (nombres, apellidos, Nusuario, Ndocumento, correo, telefono, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        user.nombre,
        user.apellido,
        user.Nusuario,
        user.Ndocumento,
        user.email,
        user.telefono,
        clave_transformada
    )
    try:
        result = execute_query(db_connection, insert_query, params)
        if not result:
            raise Exception("No se insertó ningún registro")

        logging.info("✅ Usuario insertado correctamente.")
        return {"ok": True, "mensaje": "Usuario registrado con éxito"}
    except Exception as e:
        logging.error(f"❌ Error al registrar usuario: {e}")
        return {"ok": False, "mensaje": "Error al registrar usuario"}
    finally:
        disconnect_from_mysql(db_connection)
