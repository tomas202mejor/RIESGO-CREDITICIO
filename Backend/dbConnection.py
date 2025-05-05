from dotenv import load_dotenv
import os

import mysql.connector
from mysql.connector import Error
import logging
load_dotenv()  # Esto carga las variables desde el .env

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
    "port": int(os.getenv("DB_PORT")),
}

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            logging.info("✅ Conectado a la base de datos MySQL.")
            return connection
    except Error as e:
        logging.error(f"❌ Error al conectar a la base de datos: {e}")
        return None



# Función para desconectar de la base de datos
def disconnect_from_mysql(connection):
    try:
        if connection and connection.is_connected():
            connection.close()
            logging.info("🔌 Conexión a MySQL cerrada.")
    except Error as e:
        logging.error(f"❌ Error al cerrar la conexión: {e}")

# Función para ejecutar una consulta SQL (SELECT)
def execute_query(connection, query, params=None):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        logging.info("📄 Consulta ejecutada correctamente.")
        return result
    except Error as e:
        logging.error(f"❌ Error al ejecutar la consulta: {e}")
        return None
# Ejecutar INSERT, UPDATE, DELETE
def execute_non_query(connection, query, params=None):
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()
        logging.info("✅ Consulta INSERT/UPDATE/DELETE ejecutada correctamente.")
        return True
    except Error as e:
        logging.error(f"❌ Error en consulta de modificación: {e}")
        return False

