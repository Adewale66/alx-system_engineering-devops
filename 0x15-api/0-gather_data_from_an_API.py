#!/usr/bin/python3

"""
Gather data from an api
"""

import requests
from sys import argv


if __name__ == '__main__':
    num = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    data = requests.get(f"{url}/users/{num}")
    response = data.json()
    if response:
        name = response['name']
        id = response['id']
        tasks = requests.get(f"{url}/todos?userid={id}").json()
        completed = [x for x in tasks if x['completed']]
        print(f"Employee {name} is done with tasks(\
            {len(completed)}/{len(tasks)}):")
        for task in completed:
            print("\t {}".format(task['title']))
