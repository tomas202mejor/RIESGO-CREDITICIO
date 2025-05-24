from fastapi import APIRouter, Depends, HTTPException
from schemas import ReporteCredito
from auth import get_current_user
from database import connect_to_mysql, execute_query, disconnect_from_mysql

from typing import List

router = APIRouter()

@router.get("/ConsultaCredito/{id}", response_model=List[ReporteCredito])
def get_datos_por_id(id: int, current_user: dict = Depends(get_current_user)):
    db = None
    try:
        db = connect_to_mysql()

        query_fin = """
            SELECT A.idRegistro, A.nombre, A.documento, A.vrIngresos, A.vrGastos, A.vrCredito, A.cuotas, A.estado, B.rentable, B.porcentAprobado, B.porcentRechazo
            FROM registro_financiero as A LEFT JOIN resultado_credito as B on A.idRegistro = B.idCredito
            WHERE A.idRegistro = %s
        """
        params_fin = (id,)
        result_fin = execute_query(db, query_fin, params_fin)

        reportes = []
        for datos in result_fin:
            reporte = {
                "id": datos["idRegistro"],
                "nombre": datos["nombre"],
                "documento": datos["documento"],
                "vrIngresos": datos["vrIngresos"],
                "vrGastos": datos["vrGastos"],
                "vrCredito": datos["vrCredito"],
                "numCuotas": datos["cuotas"],
                "estado": datos["estado"],
                "rentable": datos["rentable"],
                "porcentAprobado": datos["porcentAprobado"],
                "porcentRechazo": datos["porcentRechazo"]
            }
            reportes.append(reporte)

        return reportes

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        disconnect_from_mysql(db)

