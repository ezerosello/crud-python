from tkinter import *

from modules.buttonBox import *
from modules.functionsCRUD import *
from modules.entries import *

root = Tk()

class Window():
    def __init__(self, window):
        self.window = window
        self.window.title('CRUD Python')
        self.window.resizable(0,0)

        # ---- Entries ---- #
        label_search = create_label(self, 'Búsqueda por email:')
        label_name = create_label(self, 'Nombre:')
        label_last_name = create_label(self, 'Apellido:')
        label_email = create_label(self, 'Email:')
        label_password = create_label(self, 'Contraseña:')

        all_labels = [label_search, label_name, label_last_name, label_email, label_password]
        place_label(self, all_labels)

        string_search = StringVar()
        string_name = StringVar()
        string_last_name = StringVar()
        string_email = StringVar()
        string_password = StringVar()

        entry_search = create_entry(self, string_search)
        entry_name = create_entry(self, string_name)
        entry_last_name = create_entry(self, string_last_name)
        entry_email = create_entry(self, string_email)
        entry_password = create_entry(self, string_password)
        entry_password.config(show='*')

        data = [string_search, string_name, string_last_name, string_email, string_password]

        all_entries = [entry_search, entry_name, entry_last_name, entry_email, entry_password]
        place_entry(self, all_entries)

        # ---- Button Box ---- #
        button_create_database = create_button(self, 'Create\nDatabase', create_database, data)
        button_create = create_button(self, 'Create', create, data)
        button_read = create_button(self, 'Read', read, data)
        button_update = create_button(self, 'Update', update, data)
        button_delete = create_button(self, 'Delete', delete, data)

        buttons = [button_create_database, button_create, button_read, button_update, button_delete]

        place_button(self, buttons)

aplicacion = Window(root)

root.mainloop()