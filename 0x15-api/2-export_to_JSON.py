#!/usr/bin/python3
"""records all tasks that are owned by an employee"""
import json
import requests
import sys

if __name__ == "__main__":
    arg = sys.argv[1]
    response_name = requests\
        .get('https://jsonplaceholder.typicode.com/users/{}'.format(arg))
    get_todo = requests\
        .get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(arg))
    employee = response_name.json()
    employee_todo = get_todo.json()
    employee_id = employee.get('id')
    employee_name = employee.get('username')

    filename = '{}.json'.format(employee_id)

    data = []
    with open(filename, 'w') as file:
        for status in employee_todo:
            task_status = status.get('completed')
            task_title = status.get('title')
            data.append({"task": task_title,
                        "completed": task_status, "username": employee_name})
        json_data = {'{}'.format(employee_id): data}
        json.dump(json_data, file)
