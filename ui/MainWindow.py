import tkinter as tk                     
from tkinter import ttk 
import ui.tabs.GeneralTab

class MainWindow(tk.Tk):

    def __init__(self,title,size):
        super().__init__()
        self.winfo_toplevel().title(title)
        self.winfo_toplevel().geometry(size)
        self.resizable(width=False, height=False)

        self.tabcontrol = self._initialize_notebook_()
        self._add_general_tab_(self.tabcontrol)


    def _add_general_tab_ (self,tabcontrol):
        tab = tk.Frame(tabcontrol)
        tabcontrol.add(tab, text = "test")



    def _initialize_notebook_(self):
        tabcontrol = ttk.Notebook(self)
        tabcontrol.pack()
        return tabcontrol


        