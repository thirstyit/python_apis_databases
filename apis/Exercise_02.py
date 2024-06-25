'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests

req = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

text_body = req.json()

emails = [e['email'] for e in text_body['data']]

print(emails)
