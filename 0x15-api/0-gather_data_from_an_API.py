#!/usr/bin/python3
'''give employee ID'''
import requests
import sys

if __name__ == "__main__":
    arg = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(arg)
    resp_todo = requests.get('{}/todos'.format(url))
    resp_user = requests.get('{}'.format(url))

    todo_data = resp_todo.json()
    user_data = resp_user.json()

    tasks = len(todo_data)
    complete_tasks = 0
    user_name = user_data['name']

    for item in todo_data:
        if item["completed"] is True:
            complete_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, complete_tasks, tasks))
    for item in todo_data:
        if item["completed"] is True:
            print("\t {}".format(item["title"]))
