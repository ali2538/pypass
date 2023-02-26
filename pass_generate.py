import random
import string


def pass_gen(pass_length, min_digits, min_spec_chars, spec_chars=False):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-']
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    all_chars = lowercase_letters + uppercase_letters
    password_list = []
    password = ""
    if spec_chars:
        for i in range(min_spec_chars):
            password_list.append(random.choice(special_characters))

    for i in range(min_digits):
        password_list.append(random.choice(digits))

    for i in range(pass_length-(min_digits+min_spec_chars)):
        password_list.append(random.choice(all_chars))

    random.shuffle(password_list)

    for i in password_list:
        password = password + str(i)

    return password
