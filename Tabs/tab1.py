import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database


class Tab1Controller:

    def __init__(self, tab_parent):
        self.title = tk.StringVar()
        self.movie_id = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
#        self.tab.columnconfigure(0, weight=1)
        tab_parent.add(self.tab, text="Add movie")
        tk.Button(self.tab, text="Add Record to Database",
                  command=self.prompt_add_movies,
                  activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        tk.Button(self.tab, text="Delete",
                  command=lambda: [self.prompt_delete_movies1, self.prompt_delete_movies2],
                  activebackground="yellow").grid(row=7, column=1, padx=15, pady=15)

        self.titleLabelTab1 = tk.Label(self.tab, text="Movie title: ")
        self.titleLabelTab1.grid(row=0, column=0, padx=15, pady=15)

        self.dateLabelTab1 = tk.Label(self.tab, text="release date: ")
        self.dateLabelTab1.grid(row=1, column=0, padx=15, pady=15)

        self.titleLabelTab1 = tk.Label(self.tab, text="Movie ID: ")
        self.titleLabelTab1.grid(row=6, column=0, padx=15, pady=15)

        self.cal = Calendar(self.tab, selectmode='day', year=2022, month=5, day=22)
        self.cal.grid(row=1, column=1, padx=15, pady=15)

        self.titleEntryTab1 = tk.Entry(self.tab, textvariable=self.title)
        self.titleEntryTab1.grid(row=0, column=1, padx=15, pady=15)

        self.titleEntryTab1 = tk.Entry(self.tab, textvariable=self.movie_id)
        self.titleEntryTab1.grid(row=6, column=1, padx=15, pady=15)

    def prompt_add_movies(self):
        title1 = str(self.title.get())
        cal_date = self.cal.selection_get()
        database.add_movie(title1, cal_date)
        self.titleEntryTab1.delete(0, END)

    def prompt_delete_movies1(self):
        title1 = str(self.title.get())
        database.delete_movie1(title1)
        self.titleEntryTab1.delete(0, END)

    def prompt_delete_movies2(self):
        mv_id = str(self.movie_id.get())
        database.delete_movie2(mv_id)
        self.titleEntryTab1.delete(0, END)
