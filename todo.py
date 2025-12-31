def view_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks available.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def main():
    print("To-Do List Manager")
    print("2. View Tasks")
    choice = input("Enter choice: ")

    if choice == "2":
        view_tasks()

if _name_ == "_main_":
    main()