"""
2. To-Do List Application
Objective: Create a simple to-do list application that allows users to add tasks, mark them as completed, and view pending tasks.

Requirements:

Use variables and data types to store tasks and their statuses.
Implement type casting and type conversions for task IDs and user inputs.
Utilize strings for task descriptions.
Apply conditional statements to check task statuses and validate inputs.
Use for loops and while loops to iterate through tasks and display them.
Create functions with arguments and keyword arguments to add tasks, mark tasks as completed, and view pending tasks.
Optional: Implement recursion to handle nested tasks or sub-tasks.

"""

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(description: str):
    # Append a dictionary with task description and status to the list
    task = {"description": description, "completed": False}
    tasks.append(task)

# Function to mark a task as completed
def complete_task(task_id: int):
    # Mark the task at the given index as completed
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True

# Function to display pending tasks
def view_pending_tasks():
    # Print only tasks that are not completed
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"Task {i}: {task['description']}")

# Adding tasks (Example usage)
add_task("Write a blog post")
add_task("Go for a run")
add_task("Read a book")

# Mark the first task as completed
complete_task(0)

# View pending tasks
view_pending_tasks()
