#!/usr/bin/python3
"""Exporting employee's TODO list progress in a JSON document."""
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)

    ready = requests.get(url)
    the_file = ready.json()
    user = requests.get(base_url).json()
    username = user.get("username")

    data = {employee_id: [
        {"task": task.get("title"),
        "completed": task.get("completed"),
        "username": username}
            for task in the_file
            ]}

    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)

