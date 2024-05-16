from tkinter import *

from modulos.buttonBox import *
from modulos.functionsCRUD import *

root = Tk()

class Window():
    def __init__(self, window):
        self.window = window
        self.window.title('CRUD Python')
        self.window.resizable(0,0)

        button_create = create_button(self, 'Create', create)
        button_read = create_button(self, 'Read', read)
        button_update = create_button(self, 'Update', update)
        button_delete = create_button(self, 'Delete', delete)

        buttons = [button_create, button_read, button_update, button_delete]

        place_button(self, buttons)

aplicacion = Window(root)

root.mainloop()