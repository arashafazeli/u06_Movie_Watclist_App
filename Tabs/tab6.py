import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database
import datetime


class Tab6Controller:

    def __init__(self, tab_parent):
        self.username = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Show watched movies")
        tk.Button(self.tab,
                  text="View watched movies",
                  command=self.prompt_show_watched_movies,
                  activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        self.titleLabelTab6 = tk.Label(self.tab, text="Enter your username to see which movie you have watched:")
        self.titleLabelTab6.grid(row=0, column=0, padx=15, pady=15)

        self.titleEntryTab6 = tk.Entry(self.tab, textvariable=self.username)
        self.titleEntryTab6.grid(row=0, column=1, padx=15, pady=15)
#        self.tab.bind("<Return>", self.prompt_show_watched_movies)
#        self.tab.bind("<KP_Enter>", self.prompt_show_watched_movies)

    def prompt_show_watched_movies(self):
        username = str(self.username.get())
        movies = database.get_watched_movies(username)

        if movies:
            j = 0
            for movie in movies:
                text = tk.Text(self.tab, height=1)
                text.grid(row=j + 5, column=0)
                text.insert(END, movie[1])

#                e = tk.Entry(self.tab, width=100, fg='blue')
#                e.grid(row=j + 5, column=0)
#                e.insert(END, movie)
                j = j + 1
        else:
            text = tk.Text(self.tab, height=1)
            text.grid(padx=10, pady=20)
            # Insert content into the text area
            text.insert("1.0", "The user has no watched no movies yet!")
        self.titleEntryTab6.delete(0, END)

