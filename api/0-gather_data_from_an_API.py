#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys

if __name__== "__main__":

    employee_id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    base_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    ready = requests.get(url)
    the_file = ready.json()

    ready1 = requests.get(base_url).json()

    done = [item for item in the_file if item["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(ready1["name"], len(done), len(the_file)))
    for item in done:
        print("\t {}".format(item["title"]))
