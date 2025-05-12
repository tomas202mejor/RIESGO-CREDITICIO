from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    nombre: str
    telefono: str
    Ndocumento: str


    class Config:
        orm_mode = True  