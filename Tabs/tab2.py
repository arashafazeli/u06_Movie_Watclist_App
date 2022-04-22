import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database


class Tab2Controller:

    def __init__(self, tab_parent):
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="View all movies")

        self.allLabelTab2 = tk.Label(self.tab, text="ALL MOVIES")
        self.imgLabelTab2 = tk.Label(self.tab)

        self.buttonCommit = tk.Button(self.tab, text="VIEW ALL MOVIES", command=self.all_movies, activebackground="yellow")

        self.allLabelTab2.grid(row=0, column=0, padx=15, pady=15)
        self.imgLabelTab2.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)

    def all_movies(self):
        movies = database.get_movies(True)
        pl_select = tk.Listbox(self.tab, height=10, width=40)
        pl_select.grid(row=4, column=2, padx=10, pady=30)
        pl_select.insert(END, *movies)
        text_scroll = tk.Scrollbar(self.tab, orient="vertical", command=pl_select.yview)
        pl_select["yscrollcommand"] = text_scroll.set
        text_scroll.grid(row=4, column=3, sticky="ns")
