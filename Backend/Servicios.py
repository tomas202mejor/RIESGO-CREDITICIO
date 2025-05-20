from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Login import router as login_router
from registro import router as registro_router
from registroDatosFin import router as finanzas_router  
from DatosUsuario import router as usuario_router
from recuperacion import router as recuperacion_router 
from ResetPaswor import router as reset_router

from routes import user
from Consulta import router as Consulta_router
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv(dotenv_path='.venv/.env')

app = FastAPI(
    title="Microservicio de Autenticación y Registro",
    description="API para autenticación de usuarios, registro y manejo de datos financieros",
    version="1.0.0"
)

# Configurar CORS
origins = [
    os.getenv("FRONTEND_URL", "http://localhost:3000"),
    os.getenv("FRONTEND_URL_2", "http://localhost:5173"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(reset_router, prefix="/auth", tags=["Restablecer Contraseña"])
app.include_router(recuperacion_router, prefix="/auth", tags=["Recuperación de contraseña"])
app.include_router(login_router, prefix="/auth", tags=["Autenticación"])
app.include_router(registro_router, prefix="/users", tags=["Registro de Usuarios"])
app.include_router(finanzas_router, prefix="/finanzas", tags=["Finanzas"]) 
app.include_router(usuario_router, prefix="/usuario", tags=["Datos del Usuario"])
app.include_router
app.include_router(Consulta_router,prefix="/Consulta",tags=["Consulta datos del usuario"])

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def read_root():
    return {"message": "🚀 Bienvenido a la API de Autenticación, Registro y Datos Financieros"}

app.include_router(usuario_router, prefix="/usuario", tags=["Datos del Usuario"])
