import os
from dotenv import load_dotenv
import mysql.connector

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
            print("Conexión exitosa a MySQL")
            return connection
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None

def execute_query(connection, query):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as error:
            print(f"Error al ejecutar la consulta: {error}")
            return None
        finally:
            cursor.close()
    else:
        print("No hay conexión a la base de datos.")
        return None

def disconnect_from_mysql(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexión cerrada")


if __name__ == "__main__":
    db_connection = connect_to_mysql("localhost", os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_DATABASE'))

    if db_connection:

        query = "Query" 
        results = execute_query(db_connection, query)

        if results:
            for row in results:
                print(row)

        disconnect_from_mysql(db_connection)