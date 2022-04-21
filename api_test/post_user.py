import json

import requests

resp=requests.post("https://reqres.in/api/users", data=json.loads(open("data.json",'r').read()))
print(resp.json())
assert resp.json()['name']=="morpheus", "Wrong name"
