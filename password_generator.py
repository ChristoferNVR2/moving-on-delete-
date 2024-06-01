import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


num = False
spe = False
min_length_ = int(input("Enter the minimum length: "))
has_numbers_ = str(input("Do you want to have numbers? (y/n) "))
if has_numbers_.lower() == 'y':
    num = True
has_special_ = str(input("Do you want to have special characters? (y/n) "))
if has_special_.lower() == 'y':
    spe = True

password = generate_password(min_length_, num, spe)

print("The generated password is:", password)
