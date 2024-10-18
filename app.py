import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work/Personal/Urgent): ")
    task = {
        'title': title,
        'description': description,
        'category': category,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{i}. {task['title']} - {task['description']} [{task['category']}] - {status}")

def edit_task():
    view_tasks()
    task_id = int(input("Enter task number to edit: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]['title'] = input("Enter new title: ")
        tasks[task_id]['description'] = input("Enter new description: ")
        tasks[task_id]['category'] = input("Enter new category: ")
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def mark_task_completed():
    view_tasks()
    task_id = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def menu():
    print("\n--- Personal To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

tasks = load_tasks()

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        mark_task_completed()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")
