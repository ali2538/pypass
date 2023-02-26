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

        self.special_chars_option = tk.BooleanVar()
        self.special_chars_option.set(False)
        self.special_chars_checkbox = ttk.Checkbutton(self, text="!@#$%^&*", variable=self.special_chars_option,
                                                      onvalue=True, offvalue=False,
                                                      command=self.special_char_option_changed)
        self.special_chars_checkbox.grid(column=0, row=3, sticky=tk.W, padx=10)

        # password length options
        self.columnconfigure(2, weight=4)
        self.default_password_length = tk.IntVar()
        self.default_password_length.set(10)

        self.min_digits = tk.IntVar()
        self.min_digits.set(1)

        self.password_length_label = ttk.Label(self, text="Password Length")
        self.password_length_label.grid(column=2, row=0, sticky=tk.NW, padx=10, pady=(10, 0))
        self.password_length_option = ttk.Spinbox(self, from_=8, to=20, textvariable=self.default_password_length,
                                                  wrap=False, width=3)
        self.password_length_option.grid(column=2, row=0, sticky=tk.E)

        self.password_min_digit_label = ttk.Label(self, text="Minimum Digits")
        self.password_min_digit_label.grid(column=2, row=1, sticky=tk.NW, padx=10, pady=(10, 0))
        self.password_min_digit = ttk.Spinbox(self, from_=0, to=5, textvariable=self.min_digits, width=3, wrap=False)
        self.password_min_digit.grid(column=2, row=1, sticky=tk.E)

        self.min_special_chars = tk.IntVar()
        self.min_special_chars.set(0 if self.special_chars_option.get() == 0 else 1)
        self.password_min_special_chars_label = ttk.Label(self, text="Minimum Special Chars")
        self.password_min_special_chars_label.grid(column=2, row=2, sticky=tk.NW, padx=10, pady=(10, 0))
        self.password_min_special_chars = ttk.Spinbox(self, from_=0, to=5, textvariable=self.min_special_chars, width=3,
                                                      wrap=False,
                                                      state="normal" if self.special_chars_option.get() else "disabled")
        self.password_min_special_chars.grid(column=2, row=2, sticky=tk.E)

        self.btn_generate_password = ttk.Button(self, text="Generate Password", width=15,
                                                command=self.generate_password)
        self.btn_generate_password.grid(column=0, row=5, sticky=tk.W, pady=(10, 0), padx=10)

        self.btn_copy_to_clipboard = ttk.Button(self, text="Copy to Clipboard", width=15)
        self.btn_copy_to_clipboard.state(["disabled"])
        self.btn_copy_to_clipboard.grid(column=0, row=6, sticky=tk.W, pady=(10, 0), padx=10)

        self.styles.configure('TLabel', background="#d4d3d2")
        self.lbl_generated_password = ttk.Label(self, text="Generated Password", background="white", width=30)
        self.lbl_generated_password.grid(column=2, row=6, sticky=tk.W, pady=(10, 0), padx=10)

    def special_char_option_changed(self):
        if self.special_chars_option.get() == 0:
            self.min_special_chars.set(0)
            self.password_min_special_chars.config(state="disabled")
            # self.min_special_chars.
        else:
            self.min_special_chars.set(1)
            self.password_min_special_chars.config(state="normal")

    def generate_password(self):
        pass_length = self.default_password_length.get()
        special_char = self.special_chars_option.get()
        self.lbl_generated_password.config(text=pass_gen(pass_length=pass_length, min_digits=self.min_digits.get(), min_spec_chars=self.min_special_chars.get(), spec_chars=special_char))
        self.btn_copy_to_clipboard.config(state="normal")
