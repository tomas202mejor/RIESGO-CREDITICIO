from pydantic import BaseModel
from typing import Optional

class ReporteFinanciero(BaseModel):
    id: int
    nombre: str
    documento: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int
    balance: float
    estado: int
    
class UserResponse(BaseModel):
    id: int
    username: str       
    email: str
    nombre: str
    telefono: str
    Ndocumento: str


    class Config:
        orm_mode = True

class ReporteCredito(BaseModel):        
    id: int
    nombre: str
    documento: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int
    estado: int
    rentable: Optional[int] = None
    porcentAprobado: Optional[float] = None
    porcentRechazo: Optional[float] = None