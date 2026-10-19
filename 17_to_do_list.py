# Project 17: To-Do List

tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if (choice == "1"):
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif (choice == "2"):
        if (len(tasks) == 0):
            print("No tasks yet")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif (choice == "3"):
        number = int(input("Enter task number to delete: "))
        if (1 <= number <= len(tasks)):
            removed = tasks.pop(number - 1)
            print("Deleted:", removed)
        else:
            print("Invalid task number")
    elif (choice == "4"):
        print("Bye!")
        break
    else:
        print("Invalid choice")
