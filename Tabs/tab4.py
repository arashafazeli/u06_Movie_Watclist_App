import tkinter as tk
from tkinter import ttk
from tkinter import *
import database
from tkinter import messagebox as ms


class Tab4Controller:

    def __init__(self, tab_parent):
        self.username = tk.StringVar()
        self.movie_id = tk.StringVar()
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Add Watched movie")

        self.userLabelTab4 = tk.Label(self.tab, text="Username:")
        self.idLabelTab4 = tk.Label(self.tab, text="Movie Title:")

        self.userEntryTab4 = tk.Entry(self.tab, textvariable=self.username)
        self.idEntryTab4 = tk.Entry(self.tab, textvariable=self.movie_id)

        self.imgLabelTab4 = tk.Label(self.tab)

        self.buttonCommit = tk.Button(self.tab, text="Add movie to watched list", command=self.prompt_watch_movie, activebackground="yellow")

        # === ADD WIDGETS TO GRID ON TAB FOUR
        self.userLabelTab4.grid(row=0, column=0, padx=15, pady=15)
        self.userEntryTab4.grid(row=0, column=1, padx=15, pady=15)

        self.idLabelTab4.grid(row=1, column=0, padx=15, pady=15)
        self.idEntryTab4.grid(row=1, column=1, padx=15, pady=15)

        self.imgLabelTab4.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)

    def prompt_watch_movie(self):
        username = str(self.username.get())
        movie_id = str(self.movie_id.get())
        check_exist = database.exist_movie_id(int(movie_id))
        if check_exist:
            database.watch_movie(username, movie_id)
            ms.showinfo('Success!', 'Movie Added to Watched List!')
        else:
            ms.showerror('ERROR!', 'Movie ID is Not VALID!')
        self.userEntryTab4.delete(0, END)
        self.idEntryTab4.delete(0, END)









































































































































































































































































































































































































































































































































































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


