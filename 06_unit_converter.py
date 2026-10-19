# Project 6: Unit Converter

print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Kilograms to Pounds")
print("3. Meters to Feet")
choice = input("Choose 1, 2 or 3: ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    print(f"{km} km = {km * 0.621371:.2f} miles")
elif choice == "2":
    kg = float(input("Enter kilograms: "))
    print(f"{kg} kg = {kg * 2.20462:.2f} pounds")
elif choice == "3":
    m = float(input("Enter meters: "))
    print(f"{m} m = {m * 3.28084:.2f} feet")
else:
    print("Invalid choice")
