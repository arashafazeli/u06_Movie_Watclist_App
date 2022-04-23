import tkinter as tk
from tkinter import ttk

# importing all classes
from Tabs.tab1 import Tab1Controller
from Tabs.tab2 import Tab2Controller
from Tabs.tab3 import Tab3Controller
from Tabs.tab4 import Tab4Controller
from Tabs.tab5 import Tab5Controller
from Tabs.tab6 import Tab6Controller
from Tabs.tab7 import Tab7Controller
from Tabs.tab8 import Tab8Controller

# make the main window
if __name__ == '__main__':
    form = tk.Tk()
    form.title("Welcome to MWL app!")
    form.geometry("1150x900")
    tab_parent = ttk.Notebook(form)

    tab_parent.pack(expand=1, fill='both')
# make the tabs
    tab1 = Tab1Controller(tab_parent)
    tab2 = Tab2Controller(tab_parent)
    tab3 = Tab3Controller(tab_parent)
    tab4 = Tab4Controller(tab_parent)
    tab5 = Tab5Controller(tab_parent)
    tab6 = Tab6Controller(tab_parent)
    tab7 = Tab7Controller(tab_parent)
    tab8 = Tab8Controller(tab_parent)
    form.mainloop()
