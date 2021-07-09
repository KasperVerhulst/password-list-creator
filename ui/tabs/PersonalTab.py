import tkinter as tk    

class PersonalTab(tk.Frame):

    TITLE = "Personal"
    NUMBER_OF_RECORDS = 4
    MAX_NUMBER_OF_ENTRIES = 10
    NB_COLS = 3

    def __init__(self, tabcontrol):
        super().__init__(tabcontrol)

        #create three equal width columns
        for col in range(self.NB_COLS):
            self.grid_columnconfigure(col, weight=1, uniform='third')

        #create three equal width rows
        for row in range(self.MAX_NUMBER_OF_ENTRIES):
            self.grid_rowconfigure(row, weight=1, uniform='tenth')


        for entry in range(self.NUMBER_OF_RECORDS):
            self.initialize_row(entry)





    def initialize_row(self, row):
        """Add a new row to include personal details of a significant other""" 
        first_name_labelframe = tk.LabelFrame(self, text = "First Name:")
        first_name_labelframe.grid(column=0, row = row)
        first_name_entry = tk.Entry(first_name_labelframe)
        first_name_entry.insert(tk.END,"e.g. John")
        first_name_entry.pack()


        last_name_labelframe = tk.LabelFrame(self, text = "Last Name:")
        last_name_labelframe.grid(column=1, row = row)
        last_name_entry = tk.Entry(last_name_labelframe)
        last_name_entry.insert(tk.END, "e.g. Smith")
        last_name_entry.pack()


        birth_date_labelframe = tk.LabelFrame(self, text = "Birthday:")
        birth_date_labelframe.grid(column=2, row = row)
        birth_date_entry = tk.Entry(birth_date_labelframe)
        birth_date_entry.insert(tk.END,"DD-MM-YYYY")
        birth_date_entry.pack()



