#!/usr/bin/python3

"""
Export to CSV
"""

import requests
from sys import argv


if __name__ == '__main__':
    num = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    data = requests.get(f"{url}/users/{num}")
    response = data.json()
    if response:
        n = response['name']
        id = response['id']
        tasks = requests.get(f"{url}/todos?userid={id}").json()
        completed = [x for x in tasks if x['completed']]
        with open(f"{num}.csv", 'w') as f:
            for t in tasks:
                f.write(f'"{id}", "{n}", "{t["completed"]}","{t["title"]}"\n')
