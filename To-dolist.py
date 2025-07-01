tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as done: "))
        tasks[idx - 1]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: "))
        tasks.pop(idx - 1)
        print("Task deleted.")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
