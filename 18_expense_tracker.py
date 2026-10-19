# Project 18: Expense Tracker

expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spent")
    print("4. Exit")
    choice = input("Choose an option: ")

    if (choice == "1"):
        item = input("Enter item name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
        print("Expense added")
    elif (choice == "2"):
        if (len(expenses) == 0):
            print("No expenses yet")
        else:
            for e in expenses:
                print(f"{e['item']} - {e['amount']}")
    elif (choice == "3"):
        total = sum(e["amount"] for e in expenses)
        print(f"Total spent: {total}")
    elif (choice == "4"):
        print("Bye!")
        break
    else:
        print("Invalid choice")
