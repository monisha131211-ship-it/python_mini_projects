# Project 14: Random Quote Generator

import random

quotes = [
    "Small steps every day lead to big results.",
    "Mistakes are proof that you are trying.",
    "Practice makes progress.",
    "Learn something new every day.",
    "Start where you are, use what you have.",
]

while (True):
    print("\n" + random.choice(quotes))
    again = input("Another quote? (y/n): ").lower()
    if (again != "y"):
        break
