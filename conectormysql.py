import mysql.connector

def conectarDB():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",    #COMPLETAR CON SU USER DE MYSQL
        password="123456",  #COMPLETAR CON SU PASSWORD DE MYSQL
        database="skyroute"
        )
    cursor = conn.cursor()
    return conn, cursor
