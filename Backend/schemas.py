from pydantic import BaseModel

class ReporteFinanciero(BaseModel):
    nombre: str
    documento: str
    vrIngresos: float
    vrGastos: float
    vrCredito: float
    numCuotas: int
    balance: float
    
class UserResponse(BaseModel):
    id: int
    username: str        # <-- cambia Nusuario por username
    email: str
    nombre: str
    telefono: str
    Ndocumento: str


    class Config:
        orm_mode = True
