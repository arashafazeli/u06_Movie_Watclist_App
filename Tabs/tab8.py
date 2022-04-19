import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database
import datetime




class Tab8Controller:

    def __init__(self, tab_parent):
        self.title = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Show the users that watched movie")
        tk.Button(self.tab,
                  text="View usernames",
                  command=self. prompt_show_user_watched_movies,
                  activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        self.titleLabelTab8 = tk.Label(self.tab, text="Enter your movie name to see which users have watched the movie")
        self.titleLabelTab8.grid(row=0, column=0, padx=15, pady=15)

        self.titleEntryTab8 = tk.Entry(self.tab, textvariable=self.title)
        self.titleEntryTab8.grid(row=0, column=1, padx=15, pady=15)

    def prompt_show_user_watched_movies(self):
        title = str(self.title.get())
        user_name = database.SELECT_USER_THAT_WATCHED_MOVIES(title)

        if user_name:
            j = 0
            for user in user_name:
                e = Entry(self.tab, width=100, fg='blue')
                e.grid(row=j + 5, column=0)
                e.insert(END, user)
                j = j + 1
        else:
            text = tk.Text(self.tab, height=8)
            text.grid(padx=10, pady=20)
            # Insert content into the text area
            text.insert("1.0", "The user has no watched no movies yet!")
