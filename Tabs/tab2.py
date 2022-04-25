import tkinter as tk
from tkinter import ttk
from tkinter import *
import database


class Tab2Controller:

    def __init__(self, tab_parent):
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="View all movies")

        self.allLabelTab2 = tk.Label(self.tab, text="ALL MOVIES")
        self.imgLabelTab2 = tk.Label(self.tab)

        self.buttonCommit = tk.Button(self.tab, text="VIEW ALL MOVIES", command=self.all_movies, activebackground="yellow")
        # === ADD WIDGETS TO GRID ON TAB two
        self.allLabelTab2.grid(row=0, column=0, padx=15, pady=15)
        self.imgLabelTab2.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)
    # Define a funktion to show all the movies in the interface (I used this funktion in the view all movie button)

    def all_movies(self):
        movies = database.get_movies(True)
        pl_select = tk.Listbox(self.tab, height=10, width=40)
        pl_select.grid(row=4, column=2, padx=10, pady=30)
        result = []
        for item in movies:
            result.append(f'{item[0]}- {item[1]} - {item[2]}')
        pl_select.insert(END, *result)
        text_scroll = tk.Scrollbar(self.tab, orient="vertical", command=pl_select.yview)
        pl_select["yscrollcommand"] = text_scroll.set
        text_scroll.grid(row=4, column=3, sticky="ns")
