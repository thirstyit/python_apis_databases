'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''

import requests

req = requests.get("http://demo.codingnomads.co:8080/tasks_api/users")

status_code = req.status_code
encoding = req.encoding
text_body = req.content

print(status_code)
print(encoding)
print(text_body)
