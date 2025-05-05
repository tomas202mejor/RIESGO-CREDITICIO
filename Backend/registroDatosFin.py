from fastapi import APIRouter
from pydantic import BaseModel
from dbConnection import connect_to_mysql, execute_non_query, disconnect_from_mysql

router = APIRouter()

class DatosFinac(BaseModel):
    nombre: str
    documento: int
    correo: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int

@router.post("/guardarDatosFinac", tags=["Datos Financieros"])
async def guardar_datos_finac(data: DatosFinac):
    db_connection = connect_to_mysql()

    if db_connection is None:
        return {"idResp": "1", "msg": "❌ No se pudo conectar a la base de datos"}

    query = """
        INSERT INTO registro_financiero 
        (nombre, documento, correo, vrIngresos, vrGastos, vrCredito, cuotas)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data.nombre,
        data.documento,
        data.correo,
        data.vrIngresos,
        data.vrGastos,
        data.vrCredito,
        data.numCuotas
    )

    try:
        success = execute_non_query(db_connection, query, params)
        if success:
            return {"idResp": "0", "msg": "✅ Datos guardados correctamente"}
        else:
            return {"idResp": "1", "msg": "❌ Error al guardar los datos"}
    except Exception as e:
        return {"idResp": "1", "error": str(e)}
    finally:
        disconnect_from_mysql(db_connection)
