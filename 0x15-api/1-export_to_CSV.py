#!/usr/bin/python3
"""records all tasks that are owned by an employee"""
import csv
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
    filename = '{}.csv'.format(employee_id)

    with open(filename, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for status in employee_todo:
            task_status = status.get('completed')
            task_title = status.get('title')
            writer\
                .writerow([employee_id, employee_name,
                          task_status, task_title])
