from tkinter import *

def create_button(self, value, function, connection, cursor, data):
    return Button(self.window, text=value, width=10, height=2, command=lambda:function(self, connection, cursor, data))

def place_button(self, buttons):
    count = 0
    for col in range(len(buttons)):
        buttons[count].grid(row=5, column=col, padx=10, pady=20)
        count+=1