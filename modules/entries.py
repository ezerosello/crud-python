from tkinter import *

def create_label(self, value):
    return Label(self.window, text=value)

def create_entry(self, textvariable):
    return Entry(self.window, textvariable=textvariable, width=28)

def place_label(self, all_labels):
    count = 0
    for row in range(len(all_labels)):
        all_labels[count].grid(row=row, column=0, columnspan=2, pady=10)
        count += 1

def place_entry(self, all_entries):
    count = 0
    for row in range(len(all_entries)):
        all_entries[count].grid(row=row, column=2, columnspan=2, pady=10)
        count += 1