import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="credito"
    )

def execute_query(db, query, params=None):
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, params)
    
    if query.strip().lower().startswith("select"):
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    else:
        db.commit()
        cursor.close()
def disconnect_from_mysql(db):
    db.close()
