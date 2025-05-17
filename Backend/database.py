import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1221",
        database="credito"
    )

def execute_query(db, query, params=None):
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def disconnect_from_mysql(db):
    db.close()
