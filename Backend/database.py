import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
<<<<<<< HEAD
        password="1234",
=======
        password="1221",
>>>>>>> 9667c03d8008c7ceb3a45ed06e419c8191661515
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
