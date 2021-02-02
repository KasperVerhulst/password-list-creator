import tkinter as tk

class GeneralTab(tk.Frame):

    TITLE = "General"
    LANGUAGES = ["English", "Nederlands"]
    NB_COLS = 4
    NB_ROWS = 4 

    def __init__(self, tabcontrol):
        """ Main function that creates the tab with general information"""
        super().__init__(tabcontrol)

        #create four equal width columns
        for col in range(self.NB_COLS):
            self.grid_columnconfigure(col, weight=1, uniform='fourth')

        #create three equal width rows
        for row in range(self.NB_ROWS):
            self.grid_rowconfigure(row, weight=1, uniform='third')

        self.lannguage_drop_down = self.initialize_language_dropdown(self.LANGUAGES)
        self.scale = self.initalize_scale()
        self.characters_selection = self.initialize_characters_selection()


    def initialize_language_dropdown (self, languages):
        """Function to add drop down menu for language selection to the tab"""
        label = tk.Label(self, text = "Select language:")
        label.grid(row=0, column=2, ipadx= 3 , ipady=3, sticky= "e") 


        dropdown = tk.ttk.Combobox(self,values=languages)
        dropdown.current(0)
        dropdown.grid(row=0, column = 3,ipadx= 3 , ipady=3,)
        return dropdown


    def initalize_scale(self):
        """Function to add slider to select word list size to the tab"""
        label = tk.Label(self, text = "Select size:")
        label.grid(row=2, column=1,sticky="s", columnspan = 2) 
        v = tk.IntVar()  
        scale = tk.Scale(self, variable = v, from_ = 1, to = 5, orient = tk.HORIZONTAL, length=250)  
        scale.grid(row = 3, column = 1,sticky="n", columnspan = 2)
        return scale
    
    def initialize_characters_selection(self):
        """Function to add checkboxes for characters sets """
        frame_checkboxes = tk.Frame(self)
        frame_checkboxes.grid(row = 0, column = 0, rowspan = 2)
        label = tk.Label(frame_checkboxes, text = "Select character sets:")
        label.pack()
        self.bool_lowercase = tk.BooleanVar(value=True)
        self.bool_uppercase = tk.BooleanVar()
        self.bool_numbers = tk.BooleanVar()
        self.bool_symbols = tk.BooleanVar()

        def show_warning():
            if (self.bool_lowercase.get() + self.bool_uppercase.get() + self.bool_numbers.get() + self.bool_symbols.get() >=3):
                warning = tk.Label(self, text = "Warning: the more alphabets allowed, the larger the size of the created dictionary", justify = "left", wraplength="100", bg="red")
                warning.grid(row = 2, column = 0, sticky= "n")
            

        c1 = tk.Checkbutton(frame_checkboxes, text='lowercase a-z',variable = self.bool_lowercase, onvalue=True, anchor = "w", command=show_warning)
        c1.pack(fill="x")
        c2 = tk.Checkbutton(frame_checkboxes, text='uppercase A-Z',variable = self.bool_uppercase, onvalue=True, anchor = "w", command=show_warning)
        c2.pack(fill="x")
        c3 = tk.Checkbutton(frame_checkboxes, text='numbers 0-9',variable = self.bool_numbers, onvalue=True, anchor = "w", command=show_warning)
        c3.pack(fill="x")
        c4 = tk.Checkbutton(frame_checkboxes, text='symbols ?!..$',variable = self.bool_symbols, onvalue=True, anchor = "w", command=show_warning)
        c4.pack(fill="x")




        return frame_checkboxes


