import mysql.connector

def conectarDB():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="skyroute"
        )
    cursor = conn.cursor()
    return conn, cursor