import json
from operator import index

# List to store tasks
tasks = []


# Function to add a task
def add_task():
    taskname = input("Enter task name: ")
    tasks.append({"task": taskname, "done": False})
    print("Task successfully added!\n")

def delete_task():
    list_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Deleted task: {removed_task['task']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid task number!\n")

def mark_done():
    list_tasks()
    try:
        index = int(input("Enter task number to be marked done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Task '{tasks[index]['task']} marked as done!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid task number!\n")


# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks available\n")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[Done]" if task['done'] else "[Pending]"
        print(f"{i}. {status} {task['task']}")
    print("")



# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!\n")




# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    print("Tasks loaded successfully!\n")

load_tasks()
while True:
    print("[1] Add Task")
    print("[2] Delete Task")
    print("[3] Mark Task as Done")
    print("[4] List Tasks")
    print("[5] Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        save_tasks()
        break
    else:
        print("Invalid choice, please try again!\n")



