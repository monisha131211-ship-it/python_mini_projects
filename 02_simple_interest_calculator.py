# Project 2: Simple Interest Calculator

print("Simple Interest Calculator")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time (years): "))

interest = (principal * rate * time) / 100
total = principal + interest

print(f"Simple Interest = {interest:.2f}")
print(f"Total Amount    = {total:.2f}")
