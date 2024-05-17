import mysql.connector

def create_database(self, connection, cursor):
    connection = mysql.connector.connect(host="localhost", database="", user="root", password="")

    try:    
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE CRUDUSERS")
    except mysql.connector.errors.DatabaseError:
        pass
    
    cursor.execute("USE CRUDUSERS")
    try:
        cursor.execute("CREATE TABLE USERS (ID INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(50), LASTNAME VARCHAR(50), EMAIL VARCHAR(50), PASSWORD VARCHAR(20))")
        connection.commit()
    except mysql.connector.errors.ProgrammingError:
        pass

    cursor.close()
    connection.close()

def create(self, connection, cursor):
    print('create')

def read(self, connection, cursor):
    print('read')

def update(self, connection, cursor):
    print('update')

def delete(self, connection, cursor):
    print('delete')