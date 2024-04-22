#!/usr/bin/python3

"""
Dictionary of list of dictionaries
"""

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users/").json()
    tasks = requests.get(f"{url}/todos").json()
    with open(f"todo_all_employees.json", 'w') as f:
        json.dump({user['id']: [{
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        } for task in tasks if task['userId'] == user['id']]
            for user in users}, f)
