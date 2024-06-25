'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''


import requests




req = requests.delete("http://demo.codingnomads.co:8080/tasks_api/users/5027")

print(req.status_code)

req2 = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

print(req2.content)