import tkinter as tk

class GeneralTab(tk.Frame):

    TITLE = "General"
    LANGUAGES = ["English", "Nederlands"]

    def __init__(self, tabcontrol):
        super().__init__(tabcontrol)
        self.lannguage_drop_down = self.initialize_language_dropdown(self.LANGUAGES)

    def _initialize_language_dropdown_ (self, languages):
        default = tk.StringVar()
        default = languages[0]
        dropdown = tk.OptionMenu(self,default,*languages)
        dropdown.pack()
        return dropdown
