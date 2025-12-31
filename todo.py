def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added successfully!")


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
    print("1. Add Task")
    print("2. View Tasks")
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()