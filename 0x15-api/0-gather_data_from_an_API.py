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
        com = [x for x in tasks if x['completed']]
        print(f"Employee {name} is done with tasks({len(com)}/{len(tasks)}):")
        for task in com:
            print("\t {}".format(task['title']))
