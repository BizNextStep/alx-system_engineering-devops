#!/usr/bin/python3

"""
Module to gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    """
    Main function to gather data from an API
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + employee_id
    response = requests.get(url)
    tasks = response.json()
    url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    response = requests.get(url)
    employee = response.json()
    done_tasks = 0
    total_tasks = len(tasks)
    print(employee["name"] + " is done with tasks(" +
          str(done_tasks) + "/" + str(total_tasks) + "):")
    for task in tasks:
        if task["completed"]:
            done_tasks += 1
            print("\t" + task["title"])
