# Project 3: Compound Interest Calculator

print("Compound Interest Calculator")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = int(input("Enter time (years): "))

amount = principal * (1 + rate / 100) ** time
interest = amount - principal

print(f"Compound Interest = {interest:.2f}")
print(f"Total Amount      = {amount:.2f}")
