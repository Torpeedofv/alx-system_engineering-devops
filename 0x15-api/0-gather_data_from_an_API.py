#!/usr/bin/python3
"""returns information about an employee using their id"""
import requests
import sys

arg = sys.argv[1]
response_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(arg))
get_todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(arg))
employee = response_name.json()
employee_todo = get_todo.json()
employee_id = employee['id']
employee_name = employee['name']
task = 0
for i in range(len(employee_todo)):
    if employee_todo[i]['completed']:
        task += 1
print(f"Employee {employee_name} is done with\
      tasks({task}/{len(employee_todo)}):")
for i in range(len(employee_todo)):
    if employee_todo[i]['completed']:
        print(f"\t {employee_todo[i]['title']}")
