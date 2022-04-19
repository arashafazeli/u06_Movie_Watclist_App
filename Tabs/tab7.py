import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar
import database
import requests
import json


class Tab7Controller:

    def __init__(self, tab_parent):
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="View upcoming movies")

        self.allLabelTab7 = tk.Label(self.tab, text="upcoming movies")
        self.imgLabelTab7 = tk.Label(self.tab)

        self.buttonCommit = tk.Button(self.tab, text="VIEW ALL upcoming MOVIES", command=self.cs_movies)

        self.allLabelTab7.grid(row=0, column=0, padx=15, pady=15)
        self.imgLabelTab7.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
        self.buttonCommit.grid(row=4, column=1, padx=15, pady=15)

    def cs_movies(self):
        url = "https://imdb-api.com/en/API/ComingSoon/k_i4k5g19z"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        items = json.loads(response.content)["items"]

        j = 0
        for item in items:
            e = tk.Entry(self.tab, width=100, fg='blue')
            title = item['title']
            year = item['year']
            releaseState = item['releaseState']
            genres = item['genres']
            directors = item['directors']
            result = f'{title} - {year} - {releaseState} - {genres} - {directors}'
            e.grid(row=j + 5, column=0)
            e.insert(END, result)
            j = j + 1

