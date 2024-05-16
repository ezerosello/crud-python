from tkinter import *

def create_button(self, value, function):
    return Button(self.window, text=value, width=10, height=2, command=lambda:function())

def place_button(self, buttons):
    count = 0
    for col in range(0,4):
        buttons[count].grid(row=0, column=col, padx=10, pady=20)
        count+=1