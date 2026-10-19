# Project 19: Contact Book

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts (A to Z)")
    print("5. Exit")
    choice = input("Choose an option: ")

    if (choice == "1"):
        name = input("Enter name: ").title()
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact saved")
    elif (choice == "2"):
        name = input("Enter name to search: ").title()
        if (name in contacts):
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found")
    elif (choice == "3"):
        name = input("Enter name to delete: ").title()
        if (name in contacts):
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")
    elif (choice == "4"):
        if (len(contacts) == 0):
            print("No contacts yet")
        else:
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")
    elif (choice == "5"):
        print("Bye!")
        break
    else:
        print("Invalid choice")
