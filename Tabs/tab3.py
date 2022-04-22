import tkinter as tk
from tkinter import ttk
from tkinter import *
import database


class Tab3Controller:

    def __init__(self, tab_parent):
        self.search = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Search for a movie")

        self.search_term = tk.StringVar()

        self.searchLabelTab3 = tk.Label(self.tab, text="SEARCH FOR A MOVIE")
        self.titleLabelTab3 = tk.Label(self.tab, text="Movie title:")

        self.titleEntryTab3 = tk.Entry(self.tab, textvariable=self.search_term)
        self.imgLabelTab3 = tk.Label(self.tab)

        self.buttonCommit = tk.Button(self.tab, text="SEARCH", command=self.prompt_search_movies, activebackground="yellow")
        self.titleEntryTab3.delete(0, END)
        self.searchLabelTab3.grid(row=0, column=0, padx=15, pady=15)
        self.titleEntryTab3.grid(row=0, column=1, padx=15, pady=15)
        self.imgLabelTab3.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)

    def prompt_search_movies(self):
        search_term1 = self.search_term.get()
        movies = database.search_movies(search_term1)
        if movies:
            pl = tk.StringVar(value=movies)
            pl_select = tk.Listbox(self.tab, listvariable=pl, height=6, width=40)
            pl_select.grid(padx=20, pady=30)
#            text_scroll = tk.Scrollbar(self.tab, orient="vertical", command=pl_select.yview)
#            text_scroll.grid(row=5, column=1, sticky="ns")
#            pl_select["yscrollcommand"] = text_scroll.set
            self.titleEntryTab3.delete(0, END)
        else:
            text = tk.Text(self.tab, height=8)
            text.grid(padx=10, pady=10)

            # Insert content into the text area
            text.insert("1.0", "Found no movies for that search term!")
