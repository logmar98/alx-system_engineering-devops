#!/usr/bin/python3
'''give employee ID'''
import json
import requests
import sys

if __name__ == "__main__":
    for arg in range(10):
        url = "https://jsonplaceholder.typicode.com/users/{}".format(arg)
        resp_todo = requests.get('{}/todos'.format(url))
        resp_user = requests.get('{}'.format(url))

        todo_data = resp_todo.json()
        user_data = resp_user.json()

        tasks = len(todo_data)
        user_name = user_data['username']

        obj = {'{}'.format(arg): []}

        for item in todo_data:
            todo_obj = {}
            todo_obj['task'] = item["title"]
            todo_obj['completed'] = item['completed']
            todo_obj['username'] = user_name
            obj['{}'.format(arg)].append(todo_obj)

        json_data = json.dumps(obj)
        with open('all.json', 'w') as file:
            file.write(json_data)
