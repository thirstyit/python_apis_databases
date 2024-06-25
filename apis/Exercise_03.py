'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests




req = requests.post("http://demo.codingnomads.co:8080/tasks_api/users", json={
    "email": "sam@here.com",
    "first_name": "Sam",
    "last_name" : "Ferguson"
    }
)

print(req.status_code)

req2 = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

print(req2.content)