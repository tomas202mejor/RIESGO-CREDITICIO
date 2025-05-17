from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".venv/.env")

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:1234@localhost:3306/credito")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

router = APIRouter()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    Nusuario = Column(String(50), unique=True, index=True)
    Ndocumento = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    telefono = Column(String(50), unique=True, index=True)
    password = Column(String(255))

Base.metadata.create_all(bind=engine)

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
    class Config:
        from_attributes = True

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

@router.post("/registro", response_model=UserOut)
def registrar_usuario(user: UserCreate):
    db = SessionLocal()
    for campo in ["Nusuario", "Ndocumento", "email", "telefono"]:
        if db.query(User).filter(getattr(User, campo) == getattr(user, campo)).first():
            db.close()
            raise HTTPException(status_code=400, detail=f"El {campo} ya está registrado")

    user_db = User(
        nombre=user.nombre,
        apellido=user.apellido,
        Nusuario=user.Nusuario,
        Ndocumento=user.Ndocumento,
        email=user.email,
        telefono=user.telefono,
        password=hash_password(user.password)
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    db.close()
    return user_db

