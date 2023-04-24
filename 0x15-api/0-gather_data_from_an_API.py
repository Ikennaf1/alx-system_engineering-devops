#!/usr/bin/python3
"""Takes an Employee ID as argument, and returns information
about TODO list associated with the ID.
"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    # User Response
    response = requests.get(user_uri).json()

    # Employee name
    name = response.get('name')

    # TODO Response
    response = requests.get(todo_uri).json()

    # Total number of all tasks
    total = len(response)

    # Number of non-completed tasks
    not_completed = sum([elem['completed'] is False for elem in response])

    # Number of completed tasks
    completed = total - not_completed

    # Formatting output
    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(emp_name=name, completed=completed, total=total))

    # Printing completed tasks
    for elem in response:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
