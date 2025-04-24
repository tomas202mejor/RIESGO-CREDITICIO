from fastapi import FastAPI, Request
from pydantic import BaseModel
from dbConnection import connect_to_mysql, execute_query, disconnect_from_mysql
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",  # Aquí pones el origen de tu frontend (puede ser localhost o el dominio correspondiente)
]
load_dotenv(dotenv_path='.venv/.env')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class datosFinac(BaseModel):
    nombre: str
    documento: int
    correo: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int

@app.post("/guardarDatosFinac")
async def guardarDatosFinac(data: datosFinac):

    db_connection = connect_to_mysql(
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_DATABASE')
    )

    query = ("INSERT INTO registro_financiero(nombre, documento, correo, vrIngresos, vrGastos, vrCredito, cuotas) VALUES (%s, %s, %s, %s, %s, %s, %s)")

    params = (data.nombre, data.documento, data.correo, data.vrIngresos, data.vrGastos, data.vrCredito, data.numCuotas)
    
    try:
        result = execute_query(db_connection, query, params)
        return {"idResp": "0", "msg": "Datos Guardados Correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        disconnect_from_mysql(db_connection)
