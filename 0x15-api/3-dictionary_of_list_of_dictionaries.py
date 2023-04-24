#!/usr/bin/python3
"""records all tasks that are owned by an employee"""
import json
import requests
import sys

if __name__ == "__main__":
    response_name = requests\
        .get('https://jsonplaceholder.typicode.com/users/')
    get_todo = requests\
        .get('https://jsonplaceholder.typicode.com/users/{}/todos')
    employee = response_name.json()
    employee_todo = get_todo.json()
    filename = 'todo_all_employees.json'

    json_data = {}
    with open(filename, 'w') as file:
        for employ in employee:
            employee_id = employ['id']
            employee_name = employ['username']
            get_todo = requests\
                .get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(employee_id))
            employee_todo = get_todo.json()
            todo = []

            for status in employee_todo:
                task_status = status.get('completed')
                task_title = status.get('title')
                todo.append({"username": employee_name,
                            "task": task_title,
                             "completed": task_status})
            json_data = {'{}'.format(employee_id): todo}
            json.dump(json_data, file)
