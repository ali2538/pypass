import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("pyCal")
root.geometry('350x250')
root.resizable(True, True)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)
# uppercase_label = ttk.Label(root, text="A-Z")
# uppercase_label.grid(column=0, row=0, sticky=tk.NW)

option_selected = tk.IntVar()
option_selected.set(1)
option_deselected = tk.IntVar()
option_deselected.set(0)

uppercase_checkbox = ttk.Checkbutton(root, text="A-Z", variable=option_selected)
uppercase_checkbox.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)


lowercase_checkbox = ttk.Checkbutton(root, text="a-z", variable=option_selected)
lowercase_checkbox.grid(column=0, row=1, sticky=tk.W, padx=10)

digits_checkbox = ttk.Checkbutton(root, text="0-9", variable=option_selected)
digits_checkbox.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

special_chars_checkbox = ttk.Checkbutton(root, text="!@#$%^&*", variable=option_deselected)
special_chars_checkbox.grid(column=0, row=3, sticky=tk.W, padx=10)

root.mainloop()
