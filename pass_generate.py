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

    #making sure at least one lowercase and one upper case letter is included
    password_list.append(random.choice(lowercase_letters))
    password_list.append(random.choice(uppercase_letters))
    for i in range(pass_length-(min_digits+min_spec_chars)-2):
        password_list.append(random.choice(all_chars))

    random.shuffle(password_list)

    for i in password_list:
        password = password + str(i)

    return password
