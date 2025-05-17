import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1221",
    database="credito",
    port=3306
)

print("Conexión exitosa" if conn.is_connected() else "Fallo")