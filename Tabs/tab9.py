import tkinter as tk
from tkinter import ttk
from tkinter import *
import database
from tkcalendar import Calendar




class Tab9Controller:

    def __init__(self, tab_parent):
        self.title = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Update your data")
        tk.Button(self.tab,
                  text="update the movie",
#                  command=
                  activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        tk.Button(self.tab,
                  text="update username",
#                  command=
                  activebackground="yellow").grid(row=6, column=1, padx=15, pady=15)
        tk.Button(self.tab,
                  text="update watched movies",
#                  command=
                  activebackground="yellow").grid(row=8, column=1, padx=15, pady=15)