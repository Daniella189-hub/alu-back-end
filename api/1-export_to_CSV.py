#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file using a REST API."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)

    todos = requests.get(url).json()
    user = requests.get(user_url).json()
    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")])
