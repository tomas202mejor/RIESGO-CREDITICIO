import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as error:
        return None

def execute_query(connection, query, params=None):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        try:    
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                return result  # lista de tuplas
            else:
                connection.commit()
                return True
        except mysql.connector.Error as error:
            print(f"DB Error: {error}")
            return None
        finally:
            cursor.close()
    return None


def disconnect_from_mysql(connection):
    if connection and connection.is_connected():
        connection.close()
