# Project 7: Currency Converter

rates = {"USD": 83.0, "EUR": 90.0, "GBP": 105.0}

print("Currency Converter (INR to other currency)")
print("Available:", ", ".join(rates))

amount = float(input("Enter amount in INR: "))
currency = input("Convert to (USD/EUR/GBP): ").upper()

if currency in rates:
    result = amount / rates[currency]
    print(f"{amount} INR = {result:.2f} {currency}")
else:
    print("Currency not available")
