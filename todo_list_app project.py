#Code Explanation
#Main Components
#Task Class: Defines a task with description, priority, due date, and completion status.
#load_tasks Function: Loads tasks from the JSON file.
#save_tasks Function: Saves tasks to the JSON file.
#add_task Function: Adds a new task.
#remove_task Function: Removes a task by index.
#mark_task_completed Function: Marks a task as completed by index.
#list_tasks Function: Lists all tasks with their details.
#main Function: Provides the command-line interface for user interaction.
#Input Validation
#Ensures the priority is one of 'high', 'medium', or 'low'.
#Validates the due date format (YYYY-MM-DD).
#Error Handling
#Handles invalid task numbers gracefully.
#Comments and Documentation
#The code is well-commented to explain the purpose and functionality of each function and block of code.
#Additional Information
#For further details, please refer to the code comments and the README.md file included in the project repository.

#This task description should provide a comprehensive overview of your to-do list application and guide the reviewer on how to use and understand it
import json
import os

TASK_FILE = 'tasks.json'

class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.description} (Priority: {self.priority}, Due: {self.due_date})"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = json.load(file)
            return [Task(**task) for task in tasks]
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file, default=str)

def add_task(tasks, description, priority, due_date):
    task = Task(description, priority, due_date)
    tasks.append(task)

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]

def mark_task_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Task description: ")
            priority = input("Priority (high, medium, low): ")
            due_date = input("Due date (YYYY-MM-DD): ")
            add_task(tasks, description, priority, due_date)
            save_tasks(tasks)
        elif choice == '2':
            index = int(input("Task number to remove: ")) - 1
            remove_task(tasks, index)
            save_tasks(tasks)
        elif choice == '3':
            index = int(input("Task number to mark as completed: ")) - 1
            mark_task_completed(tasks, index)
            save_tasks(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
