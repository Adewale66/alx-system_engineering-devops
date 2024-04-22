#!/usr/bin/python3

"""
Gather data JSON
"""

import requests
from sys import argv
import json


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
        with open(f"{num}.json", 'w') as f:
            json.dump({num: [{
                "task": task['title'],
                "completed": task['completed'],
                "username": name
            } for task in tasks]}, f)
