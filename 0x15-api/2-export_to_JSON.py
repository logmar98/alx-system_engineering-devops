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
    user_name = user_data['username']
    
    obj = {'{}'.format(arg): []}
    
    for item in todo_data:
        obj['{}'.format(arg)]['task'] = item["title"]
        obj['{}'.format(arg)]['completed'] = item['completed']
        obj['{}'.format(arg)]['username'] = user_name

    print(obj)
