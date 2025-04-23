from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
load_dotenv(dotenv_path='.venv/.env')

app = FastAPI()

# Configuración de base de datos MySQL
DATABASE_URL = "mysql+pymysql://root:1221@localhost:3306/base_usuarios2"
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
    # Pasar la clave a mayúsculas y luego convertirla a binario
    clave_c = clave.upper()
    clave_bin = ''.join(format(ord(c), '08b') for c in clave_c)
    return clave_bin

# Crear la app
app = FastAPI(title="Microservicio de Registro de Usuario")

# Usamos Jinja2Templates para renderizar archivos HTML
templates = Jinja2Templates(directory="templates")

# Ruta para mostrar el formulario HTML
@app.get("/", response_class=HTMLResponse)
async def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

# Ruta para registrar usuario
@app.post("/registro", response_model=UserOut)
def registrar_usuario(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter(User.nombre == user.nombre).first():
        db.close()
        raise HTTPException(status_code=400, detail="El nombre ya está registrado")
    if db.query(User).filter(User.apellido == user.apellido).first():
        db.close()
        raise HTTPException(status_code=400, detail="El apellido ya está registrado")
    if db.query(User).filter(User.Nusuario == user.Nusuario).first():
        db.close()
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")
    if db.query(User).filter(User.Ndocumento == user.Ndocumento).first():
        db.close()
        raise HTTPException(status_code=400, detail="El documento ya está registrado")
    if db.query(User).filter(User.email == user.email).first():
        db.close()
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    if db.query(User).filter(User.telefono == user.telefono).first():
        db.close()
        raise HTTPException(status_code=400, detail="El telefono ya está registrado")
    

    # Transformar la clave
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


