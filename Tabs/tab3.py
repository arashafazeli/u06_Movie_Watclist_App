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

        self.titleEntryTab3 = tk.Entry(self.tab, textvariable=self.search_term)

        self.resultLabelTab3 = tk.Label(self.tab, text="RESULT: ")

        self.buttonCommit = tk.Button(self.tab, text="SEARCH", command=self.prompt_search_movies, activebackground="yellow")
        self.searchLabelTab3.grid(row=0, column=0, padx=15, pady=15)
        self.titleEntryTab3.grid(row=0, column=1, padx=15, pady=15)
        self.buttonCommit.grid(row=0, column=2, padx=15, pady=15)
        self.resultLabelTab3.grid(row=1, column=0, padx=15, pady=15)

    def prompt_search_movies(self):
        search_term1 = self.search_term.get()
        movies = database.search_movies(search_term1)
        pl_select = tk.Listbox(self.tab, height=6, width=40)
        pl_select.grid(row=1, column=1, padx=20, pady=30)
        if movies:
            result = []
            for item in movies:
                result.append(f'{item[0]}- {item[1]} - {item[2]}')
        else:
            result = ['movie not found']
        pl_select.insert(END, *result)
        text_scroll = tk.Scrollbar(self.tab, orient="vertical", command=pl_select.yview)
        pl_select["yscrollcommand"] = text_scroll.set
        text_scroll.grid(row=1, column=2, sticky="ns")
        self.titleEntryTab3.delete(0, END)

