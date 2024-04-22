#!/usr/bin/python3

"""
Exports data in the JSON format, combining user and task information
"""

import json
import requests


if __name__ == "__main__":

  # Fetch user data
  users_url = "https://jsonplaceholder.typicode.com/users"
  try:
    users_response = requests.get(users_url)
    users = users_response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching users data: {e}")
    sys.exit(1)

  # Fetch task data
  todos_url = "https://jsonplaceholder.typicode.com/todos"
  try:
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error fetching tasks data: {e}")
    sys.exit(1)

  # Combine user and task data
  todo_all = {}
  for user in users:
    task_list = []
    for task in todos:
      if task.get("userId") == user.get("id"):
        task_dict = {
          "username": user.get("username"),
          "task": task.get("title"),
          "completed": task.get("completed"),
        }
        task_list.append(task_dict)
    todo_all[user.get("id")] = task_list

  # Export data to JSON file
  with open("todo_all_employees.json", mode="w") as f:
    json.dump(todo_all, f, indent=4)

  print("Data exported successfully to todo_all_employees.json")
