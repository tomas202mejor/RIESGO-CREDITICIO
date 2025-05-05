from dotenv import load_dotenv
import os
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargar variables de entorno
load_dotenv(dotenv_path='.venv/.env')

# 📌 IMPORTANTE: usamos router, no app
router = APIRouter()

# Configuración de base de datos MySQL
DATABASE_URL = os.getenv('DATABASE_URL', "mysql+pymysql://root:123456789@localhost:3306/credito")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo SQLAlchemy
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, index=True)
    apellido = Column(String(50), unique=True, index=True)
    Nusuario = Column(String(50), unique=True, index=True)
    Ndocumento = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True) 
    telefono = Column(String(50), unique=True, index=True)   
    password = Column(String(255))

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Esquemas Pydantic
class UserCreate(BaseModel):
    nombre: str
    apellido: str
    Nusuario: str
    Ndocumento: str
    email: str
    telefono: str
    password: str

class UserOut(BaseModel):
    id: int
    nombre: str
    apellido: str
    Nusuario: str
    Ndocumento: str
    email: str
    telefono: str
    password: str

    class Config:
        from_attributes = True

# Función para transformar la clave
def transformarClave(clave: str) -> str:
    clave_c = clave.upper()
    clave_bin = ''.join(format(ord(c), '08b') for c in clave_c)
    return clave_bin

# Templates (formulario HTML)
templates = Jinja2Templates(directory="templates")

# Ruta para mostrar el formulario HTML
@router.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

# Ruta para registrar usuario
@router.post("/registro", response_model=UserOut)
def registrar_usuario(user: UserCreate):
    db = SessionLocal()

    campos_unicos = {
        'nombre': user.nombre,
        'apellido': user.apellido,
        'Nusuario': user.Nusuario,
        'Ndocumento': user.Ndocumento,
        'email': user.email,
        'telefono': user.telefono
    }

    for campo, valor in campos_unicos.items():
        if db.query(User).filter(getattr(User, campo) == valor).first():
            db.close()
            raise HTTPException(status_code=400, detail=f"El {campo} ya está registrado")

    clave_transformada = transformarClave(user.password)

    nuevo_usuario = User(
        nombre=user.nombre,
        apellido=user.apellido,
        Nusuario=user.Nusuario,
        Ndocumento=user.Ndocumento,
        email=user.email,
        telefono=user.telefono,
        password=clave_transformada
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    db.close()

    return nuevo_usuario
