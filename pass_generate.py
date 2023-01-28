import random
import string


def pass_gen(pass_length, spec_chars=False):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-']
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    all_chars = digits + lowercase_letters + uppercase_letters
    password = ""
    if spec_chars:
        all_chars = all_chars + special_characters

    for i in range(0, pass_length):
        print(random.choice(all_chars))
        password = password + random.choice(all_chars)

    return password
