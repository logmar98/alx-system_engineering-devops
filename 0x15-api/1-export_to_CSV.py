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
    user_name = user_data['name']

    
    for item in todo_data:
        if item["completed"] is True:
            print('"{}","{}","{}","{}"'.format(arg, user_name, item["completed"] item["title"]))
