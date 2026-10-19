# Project 13: Password Generator

import random
import string

print("Password Generator")
length = int(input("Enter password length (8 or more): "))

if(length < 8):
    print("Too short! Use at least 8 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print("Your password:", password)
