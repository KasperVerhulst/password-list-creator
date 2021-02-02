import tkinter as tk

class GeneralTab(tk.Frame):

    TITLE = "General"
    LANGUAGES = ["English", "Nederlands"]
    NB_COLS = 4
    NB_ROWS = 3 

    def __init__(self, tabcontrol):
        super().__init__(tabcontrol)

        #create four equal width columns
        for col in range(self.NB_COLS):
            self.grid_columnconfigure(col, weight=1, uniform='fourth')

        #create three equal width rows
        for row in range(self.NB_ROWS):
            self.grid_rowconfigure(row, weight=1, uniform='third')

        self.lannguage_drop_down = self.initialize_language_dropdown(self.LANGUAGES)
        self.scale = self.initalize_scale()

    def initialize_language_dropdown (self, languages):
        label = tk.Label(self, text = "Select language:")
        label.grid(row=0, column=2, sticky="e", padx= 5 , pady=5) 


        dropdown = tk.ttk.Combobox(self,values=languages)
        dropdown.current(0)
        dropdown.grid(row=0, column = 3)
        return dropdown


    def initalize_scale(self):
        v = tk.IntVar()  
        scale = tk.Scale(self, variable = v, from_ = 1, to = 5, orient = tk.HORIZONTAL, length=250)  
        scale.grid(row = 2, column = 1, columnspan = 2)
        return scale
    
