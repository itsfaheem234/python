import json

filename = "tasks.json"


def load_tasks():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nno tasks yet! ")
        return

    print("\n--- your tasks ---")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")


def add_task(tasks):
    task = input("\nenter a task: ")

    if task.strip() == "":
        print("task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks(tasks)
    print("task added! ")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nenter the task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("task completed! ")
        else:
            print("invalid task number.")

    except ValueError:
        print("please enter a number.")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nenter the task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"deleted: {deleted['task']} ️")
        else:
            print("invalid task number.")

    except ValueError:
        print("please enter a number.")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. view tasks")
    print("2. add task")
    print("3. complete task")
    print("4. delete task")
    print("5. exit")

    choice = input("\nchoose an option: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("goodbye! ")
        break

    else:
        print("invalid choice. try again.")
