def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added successfully.")

def main():
    print("To-Do List Manager")
    print("1. Add Task")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

if _name_ == "_main_":
    main()