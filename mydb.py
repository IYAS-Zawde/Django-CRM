import mysql.connector

# connection
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)


#prepare a cursor object
cursorobject = database.cursor()

#create a database
cursorobject.execute ("CREATE DATABASE dcrm_db")

print ("database created")

