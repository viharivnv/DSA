import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1:3306',
    user='Admin',
    passwd='Password1$')

print(mydb)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE stocks")2