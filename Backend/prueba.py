import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="credito",
    port=3306
)

print("Conexión exitosa" if conn.is_connected() else "Fallo")