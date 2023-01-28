import tkinter as tk
from tkinter import ttk
from pass_generate import pass_gen


class MainWindow(tk.Tk):

    def __init__(self, window_title):
        super().__init__()
        self.title(window_title)
        self.geometry('450x300')
        self.resizable(True, True)
        self.styles = ttk.Style(self)
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

        self.special_chars_option = tk.StringVar()
        self.special_chars_checkbox = ttk.Checkbutton(self, text="!@#$%^&*", variable=self.special_chars_option, onvalue=True, offvalue=False)
        self.special_chars_checkbox.grid(column=0, row=3, sticky=tk.W, padx=10)

        # password length options
        self.columnconfigure(2, weight=4)
        self.default_password_length = tk.IntVar()
        self.default_password_length.set(10)
        self.password_length_label = ttk.Label(self, text="Password Length")
        self.password_length_label.grid(column=2, row=0, sticky=tk.NW, padx=10, pady=(10, 0))
        self.password_length_option = ttk.Spinbox(self, from_=8, to=20, textvariable=self.default_password_length,
                                                  wrap=False)
        self.password_length_option.grid(column=2, row=1, sticky=tk.N)

        self.btn_generate_password = ttk.Button(self, text="Generate Password", width=15, command=self.generate_password)
        self.btn_generate_password.grid(column=0, row=5, sticky=tk.W, pady=(10, 0), padx=10)

        self.btn_copy_to_clipboard = ttk.Button(self, text="Copy to Clipboard", width=15)
        self.btn_copy_to_clipboard.state(["disabled"])
        self.btn_copy_to_clipboard.grid(column=0, row=6, sticky=tk.W, pady=(10, 0), padx=10)

        self.styles.configure('TLabel', background="#d4d3d2")
        self.lbl_generated_password = ttk.Label(self, text="Generated Password", background="white", width=30)
        self.lbl_generated_password.grid(column=2, row=6, sticky=tk.W, pady=(10, 0), padx=10)

    def generate_password(self):
        pass_length = self.default_password_length.get()
        special_char = self.special_chars_option.get()
        self.lbl_generated_password.config(text=pass_gen(pass_length=pass_length, spec_chars=special_char))

