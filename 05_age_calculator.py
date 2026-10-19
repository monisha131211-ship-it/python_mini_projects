# Project 5: Age Calculator

from datetime import date

print("Age Calculator")
day = int(input("Enter birth day: "))
month = int(input("Enter birth month (1-12): "))
year = int(input("Enter birth year: "))

today = date.today()
age = today.year - year

if (today.month, today.day) < (month, day):
    age = age - 1

print(f"You are {age} years old")
