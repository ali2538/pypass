import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):

    def __init__(self, window_title):
        super().__init__()
        self.title(window_title)
        self.geometry('350x250')
        self.resizable(True, True)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.option_selected = tk.IntVar()
        self.option_selected.set(1)
        self.option_deselected = tk.IntVar()
        self.option_deselected.set(0)
        self.uppercase_checkbox = ttk.Checkbutton(self, text="A-Z", variable=self.option_selected)
        self.uppercase_checkbox.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

        self.lowercase_checkbox = ttk.Checkbutton(self, text="a-z", variable=self.option_selected)
        self.lowercase_checkbox.grid(column=0, row=1, sticky=tk.W, padx=10)

        self.digits_checkbox = ttk.Checkbutton(self, text="0-9", variable=self.option_selected)
        self.digits_checkbox.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

        self.special_chars_checkbox = ttk.Checkbutton(self, text="!@#$%^&*", variable=self.option_deselected)
        self.special_chars_checkbox.grid(column=0, row=3, sticky=tk.W, padx=10)








