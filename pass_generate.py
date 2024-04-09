import random
import string


def pass_gen(
    pass_length,
    min_digits,
    min_spec_chars,
    uppercase=True,
    lowercase=True,
    spec_chars=False,
    digits=True,
):
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-"]
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    all_digits = list(string.digits)
    all_chars = []
    if uppercase:
        all_chars.extend(uppercase_letters)
    if lowercase:
        all_chars.extend(lowercase_letters)
    password_list = []
    password = ""
    if spec_chars:
        for i in range(min_spec_chars):
            password_list.append(random.choice(special_characters))
    if digits:
        for i in range(min_digits):
            password_list.append(random.choice(all_digits))

    # making sure at least one lowercase and one upper case letter is included
    # if one is only selected, or both, we need to keep the count
    min_letter = 0
    if lowercase:
        password_list.append(random.choice(lowercase_letters))
        min_letter = min_letter + 1
    if uppercase:
        password_list.append(random.choice(uppercase_letters))
        min_letter = min_letter + 1
    for i in range(pass_length - (min_digits + min_spec_chars) - min_letter):
        password_list.append(random.choice(all_chars))

    random.shuffle(password_list)

    for i in password_list:
        password = password + str(i)

    return password
