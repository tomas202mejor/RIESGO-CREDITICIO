from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy import create_engine

app = FastAPI()

# entrada de datos
class UserLogin(BaseModel):
    nombre = str
    clave =  str


def transformarClave(clave: str) -> str:
    # aqui pasamos el parametro clave entregado por el front a mayuscula sostenida y binario
    clave_c = clave.upper()
    clave_bin = ''.join(format(ord(c), '08b') for c in clave_c)
    return clave_bin

#ruta de login
@app.post("/login")
def login(user: UserLogin):
    claveTransformada = transformarClave(user.clave)

    with engine.connect() as conn:
        query = text("SELECT * FROM usuario WHERE nombre = :nombre AND clave = :clave")
        result = conn.execute(query, {"nombre": user.nombre, "clave": claveTransformada}).fetchone()

        return {"ok": result is not None}



# Configuración de la base de datos
DATABASE_URL = ""
engine = create_engine(DATABASE_URL, echo=True)


