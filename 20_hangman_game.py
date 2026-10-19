# Project 20: Hangman Game

import random

words = ["python", "pandas", "jupyter", "github", "coding"]
word = random.choice(words)

guessed = []
lives = 6

print("Hangman - guess the word!")

while lives > 0:
    display = ""
    for letter in word:
        if (letter in guessed):
            display += letter + " "
        else:
            display += "_ "
    print("\n" + display)

    if ("_" not in display):
        print("You won! The word was", word)
        break

    guess = input("Guess a letter: ").lower()

    if (guess in guessed):
        print("You already guessed that letter")
    elif (guess in word):
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

if (lives == 0):
    print("\nGame over! The word was", word)
