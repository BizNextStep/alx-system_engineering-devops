#!/usr/bin/python3

# Import libraries alphabetically
import json

# Docstring explaining the script's functionality (replace with actual description)
"""
This script processes sample task data and exports it to a JSON file.
"""


# Sample data for demonstration purposes
# This dictionary stores tasks for different users identified by their IDs.
# Each user ID maps to another dictionary containing username and task details.
# Task details include the task title and its completion status.
tasks = {
    1: {
        "Bret": [
            {"task": "Task 1", "completed": False},
            {"task": "Task 2", "completed": True},
        ]
    },
    2: {
        "Antonette": [
            {"task": "Task 3", "completed": False},
            {"task": "Task 4", "completed": True},
        ]
    },
    3: {
        "Samantha": [
            {"task": "Task 5", "completed": False},
            {"task": "Task 6", "completed": True},
        ]
    },
}


# Create a dictionary of lists of dictionaries to represent all tasks
# This new dictionary, 'all_tasks', will have user IDs as keys and lists as values.
# Each list will contain dictionaries with username, task title, and completion status.
all_tasks = {}
for user_id, user_tasks in tasks.items():
    user_tasks_list = []
    for username, user_task_list in user_tasks.items():
        for task in user_task_list:
            # Create a dictionary for each task with username, task title, and completion status
            # and append it to the user_tasks_list
            user_tasks_list.append({"username": username, "task": task["task"], "completed": task["completed"]})
    # Add the user_tasks_list (containing task details for a user) to the all_tasks dictionary
    # with the user ID as the key
    all_tasks[user_id] = user_tasks_list

# Prevent code execution when imported as a module
if __name__ == "__main__":
    # Export the data in JSON format
    with open("todo_all_employees.json", "w") as outfile:
        # Dump the 'all_tasks' dictionary containing all user tasks into a JSON file
        # with indentation for better readability
        json.dump(all_tasks, outfile, indent=4)
