#!/usr/bin/python3

"""
Gather data JSON
"""

import json
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
        with open(f"{num}.json", 'w') as f:
            json.dump({num: [{
                "task": task['title'],
                "completed": task['completed'],
                "username": name
            } for task in tasks]}, f)
