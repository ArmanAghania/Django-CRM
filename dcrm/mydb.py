import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Hitman.agent47'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE CRM')