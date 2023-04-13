import tkinter as tk
from tkinter import filedialog as fd

import pandas as pd

from models import App, vars
from gss import gss15

root = tk.Tk()

# Simply set the theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

def button(app):
    root.title("GSS-15 Scoring")
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()


def create_template():
    root.title("Select folder for GSS-15 scoring template")

    folder_selected = fd.askdirectory()
    path = f'{folder_selected}/data.csv'

    columns = ['participant_id']
    questions = [f"question_{c+1}" for c in range(15)]
    for q in questions: columns.append(q)

    df = pd.DataFrame(columns=columns)
    df.to_csv(path, index=False)


def get_data():
    root.title("Select GSS-15 datafile")
    vars.path = fd.askopenfile().name    
    root.destroy()


def main():
    app = App(root, create_template, get_data)
    button(app)

    df = pd.read_csv(vars.path)
    domains = [
               'problem',
               'duration',
               'timing',
               'regularity',
               'adequacy',
               'insomnia',
               'total'
    ]
    for d in domains: df[f"{d}_score"] = ''
    
    for i, r in df.iterrows():
        px = r['participant_id']
        answers = [r[f"question_{c+1}"] for c in range(15)]
        g = gss15(id=px, answers=answers)
        for d in domains:
            df[f"{d}_score"][i] = getattr(g, d)

    df.to_csv(vars.path, index=False)
	

if __name__ == "__main__":
    main()
