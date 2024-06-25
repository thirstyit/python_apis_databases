'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''


import requests




req = requests.put("http://demo.codingnomads.co:8080/tasks_api/users/5027", json={
    "email": "sam@here.com",
    "first_name": "Sammy",
    "last_name" : "Ferguson"
    }
)

print(req.status_code)

req2 = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

print(req2.content)