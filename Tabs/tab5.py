import tkinter as tk
from tkinter import ttk
from tkinter import *
import database
from tkinter import messagebox as ms


class Tab5Controller:

    def __init__(self, tab_parent):
        self.username = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Add Username")
        tk.Button(self.tab, text="Add User To Database", command=self.prompt_add_user, activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        tk.Button(self.tab, text="Delete",
                  command=self.prompt_delete_username,
                  activebackground="yellow").grid(row=4, column=2, padx=15, pady=15)
        self.titleLabelTab5 = tk.Label(self.tab, text="Username:  ")
        self.titleLabelTab5.grid(row=0, column=0, padx=15, pady=15)

        self.titleEntryTab5 = tk.Entry(self.tab, textvariable=self.username)
        self.titleEntryTab5.grid(row=0, column=1, padx=15, pady=15)
    # Define a function to add user and delete user in database. (I used the function in the button)

    def prompt_add_user(self):
        username = str(self.username.get())
        database.add_user(username)
        self.titleEntryTab5.delete(0, END)
        ms.showinfo('Success!', 'Username ADDED!')

    def prompt_delete_username(self):
        user = str(self.username.get())
        database.delete_username(user.lower())
        self.titleEntryTab5.delete(0, END)
        ms.showinfo('Success!', 'Username DELETED!')
