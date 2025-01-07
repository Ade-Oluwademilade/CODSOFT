#!/usr/bin/python3

import random
import string

def generatePassword():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("Password length must be at least 8.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print(f"Your generated password is: {password}")

generatePassword()