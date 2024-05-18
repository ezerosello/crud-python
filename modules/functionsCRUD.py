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

def create_database(self, string_display):
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
        messagebox.showinfo("Crear BBDD", "Base de datos creada correctamente")
    except mysql.connector.errors.ProgrammingError:
        messagebox.showinfo("Crear BBDD", "La base de datos ya existe")

    cursor.close()
    connection.close()

def create(self, data):

    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

    name = data[1].get()
    last_name = data[2].get()
    email = data[3].get()
    password = data[4].get()

    cursor.execute(f"SELECT * FROM USERS WHERE EMAIL='{email}'")

    user_found = cursor.fetchall()

    if name == '' or last_name == '' or email == '' or password == '':
        return messagebox.showerror('Error', 'Debe completar todos los campos')
    elif not (check_email(email)):
        return messagebox.showerror('Error', 'Debe ingresar un correo electrónico válido')
    elif user_found != [] and email == user_found[0][3]:
        return messagebox.showerror('Email error', 'El correo electrónico ingresado ya está registrado')
        
    cursor.execute(f"INSERT INTO USERS (NAME, LASTNAME, EMAIL, PASSWORD) VALUES ('{name}', '{last_name}', '{email}', '{password}')")    
    connection.commit()

    data[1].set('')
    data[2].set('')
    data[3].set('')
    data[4].set('')

    cursor.close()
    connection.close()

    return messagebox.showinfo("Éxito!", "Usuario creado correctamente")

def read(self, data):    
    
    try:
        connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        cursor = connection.cursor()
    except mysql.connector.errors.ProgrammingError:
        return messagebox.showerror("Error", "Debe crear la BBDD")

    email_search = data[0].get()

    cursor.execute(f"SELECT * FROM USERS WHERE EMAIL='{email_search}'")

    user_found = cursor.fetchall()

    if data[0].get() == '':
        return messagebox.showinfo("Read", "Debe ingresar una dirección de correo para buscar")
    elif user_found == []:
        data[1].set('')
        data[2].set('')
        data[3].set('')
        data[4].set('')
        return messagebox.showinfo("Read", "No hay ningún usuario registrado con esa dirección de correo")
    else:
        data[1].set(user_found[0][1])
        data[2].set(user_found[0][2])
        data[3].set(user_found[0][3])
        data[4].set(user_found[0][4])

    cursor.close()
    connection.close()

def update(self, data):

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

    cursor.execute(f"SELECT * FROM USERS WHERE EMAIL='{search_email}'")
    user_found = cursor.fetchall()
    if user_found == []:
        data[0].set('')
        return messagebox.showerror("Delete", "El usuario que quiere actualizar no existe")
    
    cursor.execute(f"UPDATE USERS SET NAME='{name}', LASTNAME='{last_name}', EMAIL='{email}', PASSWORD='{password}' WHERE EMAIL='{search_email}'")
    
    if search_email == '':
        return messagebox.showinfo("Update", "Debe ingresar el correo del usuario a modificar")
    elif name == '' or last_name == '' or email == '' or password == '':
        return messagebox.showerror('Error', 'Debe completar todos los campos')
    elif not (check_email(email)):
        return messagebox.showerror('Error', 'Debe ingresar un correo electrónico válido')
    
    connection.commit()

    data[1].set('')
    data[2].set('')
    data[3].set('')
    data[4].set('')

    cursor.close()
    connection.close()

    return messagebox.showinfo("Update", "Usuario actualizado correctamente")

def delete(self, data):
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

    if search_email == '':
        return messagebox.showinfo("Delete", "Debe ingresar el correo del usuario que desea eliminar")
    
    cursor.execute(f"SELECT * FROM USERS WHERE EMAIL='{search_email}'")

    user_found = cursor.fetchall()

    if user_found == []:
        data[0].set('')
        return messagebox.showerror("Delete", "El usuario que quiere eliminar no existe")

    cursor.close()
    connection.close()

    return messagebox.showinfo("Delete", "Usuario borrado correctamente")