from tkinter import *
from tkinter import messagebox
import mysql.connector
from email_validator import validate_email, EmailNotValidError

def check_email(email):
    try:
        v = validate_email(email)
        email = v["email"]
        return True
    except EmailNotValidError as e:
        return False

def create_database(self, connection, cursor, string_display):
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

def create(self, connection, cursor, data):

    connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
    cursor = connection.cursor()

    name = data[1].get()
    last_name = data[2].get()
    email = data[3].get()
    password = data[4].get()

    cursor.execute("SELECT * FROM USERS")

    all_users = cursor.fetchall()

    for user in all_users:
        if user[3] == email:
            return messagebox.showerror('Email error', 'El correo electrónico ingresado ya está registrado')
        
    if name == '' or last_name == '' or email == '' or password == '':
        return messagebox.showerror('Error', 'Debe completar todos los campos')
    elif not (check_email(email)):
        return messagebox.showerror('Error', 'Debe ingresar un correo electrónico válido')
        
    cursor.execute(f"INSERT INTO USERS (NAME, LASTNAME, EMAIL, PASSWORD) VALUES ('{name}', '{last_name}', '{email}', '{password}')")    
    connection.commit()

    cursor.close()
    connection.close()

    return messagebox.showinfo("Éxito!", "Usuario creado correctamente")

def read(self, connection, cursor, data):
    
    print(data[1].get())
    print(data[2].get())
    print(data[3].get())
    print(data[4].get())
    
    # connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
    # cursor = connection.cursor()

    

    # cursor.close()
    # connection.close()

def update(self, connection, cursor, data):

    print(data[1].get())
    print(data[2].get())
    print(data[3].get())
    print(data[4].get())

    # connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
    # cursor = connection.cursor()

    

    # cursor.close()
    # connection.close()

def delete(self, connection, cursor, data):
   
    print(data[1].get())
    print(data[2].get())
    print(data[3].get())
    print(data[4].get())
   
    # connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
    # cursor = connection.cursor()

    

    # cursor.close()
    # connection.close()