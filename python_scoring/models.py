from tkinter import ttk
from dataclasses import dataclass

class App(ttk.Frame):
    def __init__(self, parent, func_1, func_2):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        self.func_1 = func_1
        self.func_2 = func_2
        self.path = ''

        # Create widgets :)
        self.setup_widgets()
    
    def select_data(self):
        self.path = self.func_2()

    def setup_widgets(self):
        # Create a Frame for the Buttons
        self.radio_frame = ttk.LabelFrame(self, text="Data Selection", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Buttons
        self.create_template = ttk.Button(
            self.radio_frame,
            text="Create Template",
            style="Accent.TButton",
            command=self.func_1
        )
        self.create_template.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        self.select_data = ttk.Button(
            self.radio_frame,
            text="Select Datafile",
            style="Accent.TButton",
            command=self.select_data
        )
        self.select_data.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

@dataclass
class vars():
    path = str

if __name__ == "__main__":
    print('This is not a standalone')
