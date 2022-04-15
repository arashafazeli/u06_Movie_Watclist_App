import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database


class Tab1Controller:

    def __init__(self, tab_parent):
        self.title = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Add movie")
        tk.Button(self.tab, text="Add Record to Database", command=self.prompt_add_movies, activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)

        self.titleLabelTab1 = tk.Label(self.tab, text="Movie title: ")
        self.titleLabelTab1.grid(row=0, column=0, padx=15, pady=15)

        self.dateLabelTab1 = tk.Label(self.tab, text="release date: ")
        self.dateLabelTab1.grid(row=1, column=0, padx=15, pady=15)

        self.cal = Calendar(self.tab, selectmode='day', year=2020, month=5, day=22)
        self.cal.grid(row=1, column=1, padx=15, pady=15)

        self.titleEntryTab1 = tk.Entry(self.tab, textvariable=self.title)
        self.titleEntryTab1.grid(row=0, column=1, padx=15, pady=15)

    def prompt_add_movies(self):
        title1 = str(self.title.get())
        cal_date = self.cal.selection_get()
        database.add_movie(title1, cal_date)
        self.titleEntryTab1.delete(0, END)

