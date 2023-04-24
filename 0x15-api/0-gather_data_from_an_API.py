#!/usr/bin/python3
"""Returns information about an employee using their id."""
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
    employee_name = employee.get('name')
    task = 0
    length = len(employee_todo)
    for i in range(length):
        if employee_todo[i].get('completed'):
            task += 1
    print(f"Employee {employee_name} is done with\
          tasks({task}/{length}):")
    for i in range(length):
        if employee_todo[i].get('completed'):
            print(f"\t {employee_todo[i].get('title')}")
