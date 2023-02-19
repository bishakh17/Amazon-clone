import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5503",
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE ecommerce")