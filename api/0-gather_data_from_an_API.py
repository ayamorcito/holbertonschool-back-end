#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """


import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    done_tasks = 0
    total_tasks = 0

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_name = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()['name']

    for task in user_tasks:
        total_tasks += 1
        if task['completed'] is True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, done_tasks, total_tasks))

    for task in user_tasks:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
