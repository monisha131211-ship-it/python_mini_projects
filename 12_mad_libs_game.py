# Project 12: Mad Libs Game

print("Mad Libs - fill in the blanks!")
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
adjective = input("Enter an adjective: ")

story = (f"One day, {name} went to {place}. "
         f"There, a {adjective} {animal} was eating {food}. "
         f"{name} laughed so much and went back home!")

print("\nYour story:")
print(story)
