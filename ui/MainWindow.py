import tkinter as tk                     
from tkinter import ttk 
from ui.tabs.GeneralTab import GeneralTab
from ui.tabs.PersonalTab import PersonalTab

class MainWindow(tk.Tk):

    def __init__(self,title,size):
        super().__init__()
        self.winfo_toplevel().title(title)
        self.winfo_toplevel().geometry(size)
        self.resizable(width=False, height=False)

        self.tabcontrol = self._initialize_notebook_()
        self._add_general_tab_(self.tabcontrol)
        self._add_personal_tab_(self.tabcontrol)


    def _add_general_tab_ (self,tabcontrol):
        tab = GeneralTab(tabcontrol)
        tabcontrol.add(tab, text = GeneralTab.TITLE)

    def _add_personal_tab_ (self,tabcontrol):
        tab = PersonalTab(tabcontrol)
        tabcontrol.add(tab, text = PersonalTab.TITLE)


    def _initialize_notebook_(self):
        customed_style = ttk.Style()
        customed_style.configure('Custom.TNotebook.Tab', padding=[5, 3], font=('Helvetica', 10))
        customed_style.configure('Custom.TNotebook', tabposition='nw')
        tabcontrol = ttk.Notebook(self, style='Custom.TNotebook')
        tabcontrol.pack(fill="both", expand=True)
        return tabcontrol


        