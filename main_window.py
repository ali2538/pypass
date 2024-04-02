import tkinter as tk
from tkinter import ttk
from pass_generate import pass_gen


class MainWindow(tk.Tk):
    def __init__(self, window_title):
        super().__init__()
        self.title(window_title)
        self.geometry("950x600")
        self.resizable(True, True)
        self.styles = ttk.Style(self)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.option_selected = tk.IntVar()
        self.option_selected.set(1)
        self.option_deselected = tk.IntVar()
        self.option_deselected.set(0)
        self.password_generated = False
        self.generated_password = tk.StringVar()
        self.generated_password.set("")

        self.uppercase_option = tk.BooleanVar()
        self.uppercase_option.set(True)
        self.uppercase_checkbox = ttk.Checkbutton(
            self,
            text="A-Z",
            variable=self.uppercase_option,
            command=self.uppercase_option_changed,
        )
        self.uppercase_checkbox.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

        self.lowercase_option = tk.BooleanVar()
        self.lowercase_option.set(True)
        self.lowercase_checkbox = ttk.Checkbutton(
            self,
            text="a-z",
            variable=self.lowercase_option,
            command=self.lowercase_option_changed,
        )
        self.lowercase_checkbox.grid(column=0, row=1, sticky=tk.W, padx=10)

        self.digits_option = tk.BooleanVar()
        self.digits_option.set(True)
        self.digits_checkbox = ttk.Checkbutton(
            self,
            text="0-9",
            variable=self.digits_option,
            command=self.digits_options_changed,
        )
        self.digits_checkbox.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

        self.special_chars_option = tk.BooleanVar()
        self.special_chars_option.set(False)
        self.special_chars_checkbox = ttk.Checkbutton(
            self,
            text="!@#$%^&*",
            variable=self.special_chars_option,
            onvalue=True,
            offvalue=False,
            command=self.special_char_option_changed,
        )
        self.special_chars_checkbox.grid(column=0, row=3, sticky=tk.W, padx=10)

        # password length options
        self.columnconfigure(2, weight=4)
        self.password_length = tk.IntVar()
        self.password_length.set(10)

        # the following variable is for keeping track of how much users can increase the options
        # we need to avoid going over password length
        # there are also minimum of other options, especially lowercase and uppercase letters that need to be calculated
        self.min_letter = 2  # min 1 lowercase and 1 uppercase
        self.remaining_options_range = tk.IntVar()
        self.remaining_options_range.set(self.password_length.get() - self.min_letter)
        self.password_length_label = ttk.Label(self, text="Password Length")
        self.password_length_label.grid(
            column=2, row=0, sticky=tk.NW, padx=10, pady=(10, 0)
        )
        self.password_length_option = ttk.Spinbox(
            self,
            from_=8,
            to=30,
            textvariable=self.password_length,
            wrap=False,
            width=3,
            command=self.update_remaining_char_options,
        )
        self.password_length_option.grid(column=2, row=0, sticky=tk.E)

        self.min_digits = tk.IntVar()
        self.min_digits.set(1)

        # update remaining range
        self.remaining_options_range.set(
            self.remaining_options_range.get() - self.min_digits.get()
        )

        self.password_min_digit_label = ttk.Label(self, text="Minimum Digits")
        self.password_min_digit_label.grid(
            column=2, row=1, sticky=tk.NW, padx=10, pady=(10, 0)
        )
        self.password_min_digit = ttk.Spinbox(
            self,
            from_=0,
            to=self.remaining_options_range.get(),
            textvariable=self.min_digits,
            width=3,
            wrap=False,
            state="normal" if self.min_digits.get() else "disabled",
            command=self.update_remaining_char_options,
        )
        self.password_min_digit.grid(column=2, row=1, sticky=tk.E)

        self.min_special_chars = tk.IntVar()
        self.min_special_chars.set(0 if self.special_chars_option.get() == 0 else 1)
        self.password_min_special_chars_label = ttk.Label(
            self, text="Minimum Special Chars"
        )
        self.password_min_special_chars_label.grid(
            column=2, row=2, sticky=tk.NW, padx=10, pady=(10, 0)
        )
        self.password_min_special_chars = ttk.Spinbox(
            self,
            from_=0,
            to=self.remaining_options_range.get(),
            textvariable=self.min_special_chars,
            width=3,
            wrap=False,
            state="normal" if self.special_chars_option.get() else "disabled",
            command=self.update_remaining_char_options,
        )
        self.password_min_special_chars.grid(column=2, row=2, sticky=tk.E)

        self.btn_generate_password = ttk.Button(
            self, text="Generate Password", width=25, command=self.generate_password
        )
        self.btn_generate_password.grid(
            column=0, row=5, sticky=tk.W, pady=(10, 0), padx=10
        )

        self.btn_copy_to_clipboard = ttk.Button(
            self, text="Copy to Clipboard", width=25, command=self.copy_to_clipboard
        )
        self.btn_copy_to_clipboard.state(["disabled"])
        self.btn_copy_to_clipboard.grid(
            column=0, row=6, sticky=tk.W, pady=(10, 0), padx=10
        )

        self.btn_clear_password = ttk.Button(
            self, text="Clear Password", width=25, command=self.clear_password
        )
        self.btn_clear_password.state(["disabled"])
        self.btn_clear_password.grid(
            column=0, row=7, sticky=tk.W, pady=(10, 0), padx=10
        )

        self.styles.configure("TLabel", background="#d4d3d2")
        self.lbl_generated_password = ttk.Label(
            self,
            textvariable=self.generated_password,
            text="Generated Password",
            background="white",
            width=30,
        )
        self.lbl_generated_password.grid(
            column=2, row=6, sticky=tk.W, pady=(10, 0), padx=10
        )

    def special_char_option_changed(self):
        if self.special_chars_option.get() == 0:
            self.min_special_chars.set(0)
            self.password_min_special_chars.config(state="disabled")
            if self.password_generated:
                self.regen_password()
        else:
            self.min_special_chars.set(1)
            self.password_min_special_chars.config(state="normal")
            if self.password_generated:
                self.regen_password()

    def generate_password(self):
        self.generated_password.set(
            pass_gen(
                pass_length=self.password_length.get(),
                min_digits=self.min_digits.get(),
                min_spec_chars=self.min_special_chars.get(),
                lowercase=self.lowercase_option.get(),
                uppercase=self.uppercase_option.get(),
                spec_chars=self.special_chars_option.get(),
            )
        )

        self.password_generated = True
        self.btn_copy_to_clipboard.config(state="normal")
        self.btn_clear_password.config(state="normal")

    def update_remaining_char_options(self):
        new_limit = (
            self.password_length.get()
            - self.min_letter
            - self.min_digits.get()
            - self.min_special_chars.get()
        )
        self.remaining_options_range.set(new_limit)
        self.password_min_special_chars.config(to=self.remaining_options_range.get())
        self.password_min_digit.config(to=self.remaining_options_range.get())
        if self.password_generated:
            self.regen_password()

    def clear_password(self):
        self.generated_password.set("")

    def regen_password(self):
        self.generated_password.set(
            pass_gen(
                pass_length=self.password_length.get(),
                min_digits=self.min_digits.get(),
                min_spec_chars=self.min_special_chars.get(),
                lowercase=self.lowercase_option.get(),
                uppercase=self.uppercase_option.get(),
                spec_chars=self.special_chars_option.get(),
            )
        )

    def digits_options_changed(self):
        if self.digits_option.get() == 0:
            self.min_digits.set(0)
            self.password_min_digit.config(state="disabled")
            if self.password_generated:
                self.regen_password()
        else:
            self.min_digits.set(1)
            self.password_min_digit.config(state="normal")
            if self.password_generated:
                self.regen_password()

    def lowercase_option_changed(self):
        if self.uppercase_option.get() == 0:
            self.uppercase_option.set(True)
            self.min_letter = 1
        if self.password_generated:
            self.regen_password()

    def uppercase_option_changed(self):
        if self.lowercase_option.get() == 0:
            self.lowercase_option.set(True)
            self.min_letter = 1
        if self.password_generated:
            self.regen_password()

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.generated_password.get())
