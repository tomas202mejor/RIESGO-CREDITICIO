from fastapi import APIRouter, Depends, HTTPException
from schemas import ReporteFinanciero
from auth import get_current_user
from database import connect_to_mysql, execute_query, disconnect_from_mysql

from typing import List

router = APIRouter()

@router.get("/Consulta", response_model=List[ReporteFinanciero])
def get_datos_financieros(current_user: dict = Depends(get_current_user)):
    db = None
    try:
        db = connect_to_mysql()

        # Obtener el Ndocumento desde la tabla users usando id del token
        query_doc = "SELECT Ndocumento FROM users WHERE id = %s"
        params_doc = (current_user["id_usuario"],)
        result_doc = execute_query(db, query_doc, params_doc)

        if not result_doc:
            raise HTTPException(status_code=404, detail="Documento no encontrado para el usuario")

        documento = result_doc[0]["Ndocumento"]
        print("📄 Documento del usuario:", documento)

        # Consultar los datos financieros con el documento
        query_fin = """
            SELECT idRegistro, nombre, documento, vrIngresos, vrGastos, vrCredito, cuotas, estado
            FROM registro_financiero
            WHERE documento = %s
        """
        params_fin = (documento,)
        result_fin = execute_query(db, query_fin, params_fin)

        if not result_fin:
            raise HTTPException(status_code=404, detail="Datos financieros no encontrados")

        reportes = []
        for datos in result_fin:
            balance = datos["vrIngresos"] - datos["vrGastos"] - datos["vrCredito"]

            reporte = {
                "id": datos["idRegistro"],
                "nombre": datos["nombre"],
                "documento": datos["documento"],
                "vrIngresos": datos["vrIngresos"],
                "vrGastos": datos["vrGastos"],
                "vrCredito": datos["vrCredito"],
                "numCuotas": datos["cuotas"],
                "balance": balance,
                "estado": datos["estado"]
            }
            reportes.append(reporte)

        return reportes

    except HTTPException as http_ex:
        raise http_ex  # Re-lanza errores controlados como 404

    except Exception as e:
        print("❌ Error inesperado:", e)
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

    finally:
        disconnect_from_mysql(db)
