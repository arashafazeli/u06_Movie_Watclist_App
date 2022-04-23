
import tkinter as tk
from tkinter import ttk
from tkinter import *
import database





class Tab8Controller:

    def __init__(self, tab_parent):
        self.title = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Show the users that watched movie")
        tk.Button(self.tab,
                  text="View usernames",
                  command=self. prompt_show_user_watched_movies,
                  activebackground="yellow").grid(row=4, column=0, padx=15, pady=15)
        self.titleLabelTab8 = tk.Label(self.tab, text="Enter your movie name to see which users have watched the movie")
        self.titleLabelTab8.grid(row=0, column=0, padx=15, pady=15)

        self.titleEntryTab8 = tk.Entry(self.tab, textvariable=self.title)
        self.titleEntryTab8.grid(row=0, column=1, padx=15, pady=15)

    def prompt_show_user_watched_movies(self):
        title = str(self.title.get())
        user_name = database.get_user_watched_movies(title.lower())
        users = tk.StringVar(value='')
        pl_select = tk.Listbox(self.tab, listvariable=users, height=10, width=40)
        pl_select.grid(row=4, column=1, padx=10, pady=30)
        text_scroll = tk.Scrollbar(self.tab, orient="vertical", command=pl_select.yview)
        pl_select["yscrollcommand"] = text_scroll.set
        text_scroll.grid(row=4, column=3, sticky="ns")
        if user_name:

            pl_select.insert(END, f'{title}:')
            pl_select.insert(END, *user_name)
            self.titleEntryTab8.delete(0, END)
        else:
            text = tk.Text(self.tab, height=5)
            text.grid(padx=10, pady=10)
            text.insert("1.0", f"{title} movie is not in our database")
            self.titleEntryTab8.delete(0, END)
