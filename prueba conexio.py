from dotenv import load_dotenv
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv(dotenv_path='.venv/.env')  # si el .env está dentro de .venv


load_dotenv()

try:
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        port=int(os.getenv("DB_PORT", 3306))
    )
    print("✅ Conexión exitosa a la base de datos.")
except mysql.connector.Error as err:
    print(f"❌ Error de conexión: {err}")
