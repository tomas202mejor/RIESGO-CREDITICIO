# registroDatosFin.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from auth import obtener_usuario_desde_token
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".venv/.env")

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:1221@localhost:3306/credito")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

router = APIRouter()

# Modelo de la tabla financiera
class RegistroFinanciero(Base):
    __tablename__ = "registro_financiero"
    idRegistro  = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    documento = Column(String(50))
    correo = Column(String(100))
    vrIngresos = Column(Float)
    vrGastos = Column(Float)
    vrCredito = Column(Float)
    cuotas = Column(Integer)

Base.metadata.create_all(bind=engine)

# Esquema de entrada
class DatosFinac(BaseModel):
    nombre: str
    documento: str
    correo: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int

@router.post("/guardarDatosFinac", tags=["Datos Financieros"])
def guardar_datos_finac(data: DatosFinac, usuario=Depends(obtener_usuario_desde_token)):
    db = SessionLocal()

    nuevo = RegistroFinanciero(
        nombre=data.nombre,
        documento=data.documento,
        correo=data.correo,
        vrIngresos=data.vrIngresos,
        vrGastos=data.vrGastos,
        vrCredito=data.vrCredito,
        cuotas=data.numCuotas
    )

    try:
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return {"idResp": "0", "msg": "✅ Datos financieros guardados correctamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"❌ Error al guardar: {str(e)}")
    finally:db.close()