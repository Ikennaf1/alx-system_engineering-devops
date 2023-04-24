#!/usr/bin/python3
"""Export data obtained from API to CSV
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # if argument can convert to digit
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted names to API uris and filenames
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # User Response
    response = requests.get(user_uri).json()

    # Employee username
    username = response.get('username')

    # User TODO Response
    response = requests.get(todo_uri).json()

    # Save user info to file
    # Filename example: `{user_id}.csv`
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in response:
            # Get completed tasks
            status = elem.get('completed')

            # Task name
            title = elem.get('title')

            # Write each result to a CSV row
            writer.writerow([emp_id, username, status, title])
