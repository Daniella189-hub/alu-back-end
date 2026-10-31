#!/usr/bin/python3
"""Exporting employee's TODO list progress in a JSON document."""
import json
import requests
import sys

if __name__ == "__main__":


    base = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for todo in todos:

            if todo.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
        data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
