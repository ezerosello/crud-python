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

    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

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
    
    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

    cursor.execute("SELECT * FROM USERS")

    all_users = cursor.fetchall()

    for user in all_users:
        if user[3] == data[0].get():
            data[1].set(user[1])
            data[2].set(user[2])
            data[3].set(user[3])
            data[4].set(user[4])

    cursor.close()
    connection.close()

def update(self, connection, cursor, data):

    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

    search_email = data[0].get()
    name = data[1].get()
    last_name = data[2].get()
    email = data[3].get()
    password = data[4].get()
    
    cursor.execute(f"UPDATE USERS SET NAME='{name}', LASTNAME='{last_name}', EMAIL='{email}', PASSWORD='{password}' WHERE EMAIL='{search_email}'")
    
    if name == '' or last_name == '' or email == '' or password == '':
        return messagebox.showerror('Error', 'Debe completar todos los campos')
    elif not (check_email(email)):
        return messagebox.showerror('Error', 'Debe ingresar un correo electrónico válido')
    
    connection.commit()

    cursor.close()
    connection.close()

    return messagebox.showinfo("Update", "Usuario actualizado correctamente")

def delete(self, connection, cursor, data):
    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

    search_email = data[0].get()

    cursor.execute(f"DELETE FROM USERS WHERE EMAIL='{search_email}'")
    connection.commit()

    data[1].set('')
    data[2].set('')
    data[3].set('')
    data[4].set('')

    cursor.close()
    connection.close()

    return messagebox.showinfo("Delete", "Usuario borrado correctamente")