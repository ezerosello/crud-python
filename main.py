from tkinter import *
import mysql.connector

from modules.buttonBox import *
from modules.functionsCRUD import *
from modules.entries import *

root = Tk()

class Window():
    def __init__(self, window):
        self.window = window
        self.window.title('CRUD Python')
        self.window.resizable(0,0)

        # ---- Database connection ---- #
        try:
            connection = mysql.connector.connect(host="localhost", database="CRUDUSERS", user="root", password="")
        except mysql.connector.errors.ProgrammingError:
            connection = mysql.connector.connect(host="localhost", database="", user="root", password="")

        cursor = connection.cursor()

        # ---- Entries ---- #
        label_search = create_label(self, 'Búsqueda por email:')
        label_name = create_label(self, 'Nombre:')
        label_last_name = create_label(self, 'Apellido:')
        label_email = create_label(self, 'Email:')
        label_password = create_label(self, 'Contraseña:')

        all_labels = [label_search, label_name, label_last_name, label_email, label_password]
        place_label(self, all_labels)

        entry_search = create_entry(self)
        entry_name = create_entry(self)
        entry_last_name = create_entry(self)
        entry_email = create_entry(self)
        entry_password = create_entry(self)
        entry_password.config(show='*')

        all_entries = [entry_search, entry_name, entry_last_name, entry_email, entry_password]
        place_entry(self, all_entries)

        # ---- Button Box ---- #

        button_create_database = create_button(self, 'Create\nDatabase', create_database, connection, cursor)
        button_create = create_button(self, 'Create', create, connection, cursor)
        button_read = create_button(self, 'Read', read, connection, cursor)
        button_update = create_button(self, 'Update', update, connection, cursor)
        button_delete = create_button(self, 'Delete', delete, connection, cursor)

        buttons = [button_create_database, button_create, button_read, button_update, button_delete]

        place_button(self, buttons)

        # ---- Close connection ---- #

        cursor.close()
        connection.close()

aplicacion = Window(root)

root.mainloop()