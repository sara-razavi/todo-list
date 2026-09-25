# Name: Sara Razavi
# Student ID: 970050118
# Project date: January 2020
# Focus: functions, lists, loops, menu systems and basic file handling

tasks = []

def show_tasks():
    print("\n---------- TASKS ----------")

    if len(tasks) == 0:
        print("There are no tasks.")
        return

    for i in range(len(tasks)):
        print(str(i + 1) + ".", tasks[i])

def add_task():
    task = input("Write a new task: ").strip()

    if task == "":
        print("You didn't write anything.")
    else:
        tasks.append(task)
        print("Task added.")

def delete_task():
    show_tasks()

    if len(tasks) == 0:
        return

    number = input("Which task should be deleted? ")

    if number.isdigit():
        number = int(number)

        if number >= 1 and number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Deleted:", removed)
        else:
            print("Wrong task number.")
    else:
        print("Please enter a number.")

def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()
    print("Tasks saved.")

def load_tasks():
    try:
        file = open("tasks.txt", "r")

        for line in file:
            line = line.strip()
            if line != "":
                tasks.append(line)

        file.close()
    except FileNotFoundError:
        # First time running the program, there may not be a file.
        pass

load_tasks()

while True:
    print("\n==========================")
    print("       MY TO-DO LIST")
    print("==========================")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save tasks")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        save_tasks()

    elif choice == "5":
        save_tasks()
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")

# I tried not to make it too complicated.
