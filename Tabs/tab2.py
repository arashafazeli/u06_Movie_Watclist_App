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

        self.buttonCommit = tk.Button(self.tab, text="VIEW ALL MOVIES", command=self.all_movies)

        self.allLabelTab2.grid(row=0, column=0, padx=15, pady=15)
        self.imgLabelTab2.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)

    def all_movies(self):
        movies = database.get_movies(True)
    #    j = 0
    #    for j in range(len(movies)):
    #        e = Entry(tab2, width=20, fg='blue')
    #        e.grid(row=j+5, column=1)
    #        e.insert(END, movies[j])
    #    j = j + 1
        pl = tk.StringVar(value=movies)
        pl_select = tk.Listbox(self.tab, listvariable=pl, height=20, width=40)
        pl_select.grid(row=4, column=2, padx=10, pady=30)

