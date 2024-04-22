#!/usr/bin/python3

"""
Module to export data to CSV
"""
import requests
import csv
import sys


if __name__ == "__main__":
    """
    Main function to export data to CSV
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + employee_id
    response = requests.get(url)
    tasks = response.json()
    url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    response = requests.get(url)
    employee = response.json()
    filename = employee_id + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'USER_ID': employee_id,
                             'USERNAME': employee["name"],
                             'TASK_COMPLETED_STATUS': task["completed"],
                             'TASK_TITLE': task["title"]})
