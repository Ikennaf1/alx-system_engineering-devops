#!/usr/bin/python3
"""Export data from an API to JSON format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    # if argument can convert to digit
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    # User Response
    user_res = requests.get(user_uri).json()

    # User TODO Response
    todo_res = requests.get(todo_uri).json()

    # A list of all tasks of an user
    u_tasks = list()

    for elem in todo_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_res.get('username')
        }

        u_tasks.append(data)

    # Create the new file for the user to save the information
    # Filename example: `{user_id}.json`
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: u_tasks}))
