from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from pydantic import BaseModel
import pandas as pd
import joblib
from database import connect_to_mysql, execute_query, disconnect_from_mysql

router = APIRouter()

class DatosEvaluacion(BaseModel):
    idCredito: int
    ingresos: float
    gastos: float
    credito: float
    cuotas: int

@router.post("/evaluarCredito")
def evaluar_credito(data: DatosEvaluacion, current_user: dict = Depends(get_current_user)):

    modelo = joblib.load("modelo_credito.pkl")
    nuevo_registro = {
        "ingresos": data.ingresos,
        "gastos": data.gastos,
        "monto_credito": data.credito,
        "cuotas": data.cuotas
    }

    df_nuevo = pd.DataFrame([nuevo_registro])

    df_nuevo["capacidad_ahorro"] = df_nuevo["ingresos"] - df_nuevo["gastos"]
    df_nuevo["cuota_aprox"] = df_nuevo["monto_credito"] / df_nuevo["cuotas"]
    df_nuevo["cuota_sobre_ingresos"] = df_nuevo["cuota_aprox"] / df_nuevo["ingresos"]

    X_nuevo = df_nuevo[["ingresos", "gastos", "monto_credito", "cuotas", "capacidad_ahorro", "cuota_sobre_ingresos"]]

    prediccion = modelo.predict(X_nuevo)
    probabilidades = modelo.predict_proba(X_nuevo)[0]

    resultado = int(prediccion[0])
    if(resultado == 1):
        decision = 'Aprobado' 
    else:
        decision = 'Rechazado'
    
    
    porcentajeAprobado = float(probabilidades[1] * 100)
    porcentajeRechazo = float(probabilidades[0] * 100)


    db = None
    try:
        db = connect_to_mysql()

        query_fin = """
            insert into resultado_credito (idCredito,rentable,porcentAprobado,porcentRechazo) values(%s,%s,%s,%s)
        """
        params_fin = (data.idCredito,resultado,porcentajeAprobado,porcentajeRechazo)
        result_fin = execute_query(db, query_fin, params_fin)

        query_fin = """
            update registro_financiero set estado = 1 where idRegistro = %s
        """
        params_fin = (data.idCredito,)
        result_fin = execute_query(db, query_fin, params_fin)

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        disconnect_from_mysql(db)

    return{
            "rentable": resultado,
            "decision": decision,
            "aprobado": porcentajeAprobado,
            "rechazado": porcentajeRechazo
        }
