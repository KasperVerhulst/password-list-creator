import tkinter as tk

class GeneralTab(tk.Frame):

    TITLE = "General"

    def __init__(self,languages):
        self.lannguage_drop_down = initialize_language_dropdown(languages)
        self.size_scale = initialize_size_selector()


    def initialize_language_dropdown (self, languages):
        default = tk.StringVar()
        default = languages[0]
        dropdown = tk.OptionMenu(self,default,*languages)

        return 0

    def initialize_size_selector():
        return 0