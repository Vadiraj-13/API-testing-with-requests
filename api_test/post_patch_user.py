import requests
import json


payload={
    "name": "AP"
    #"job": "zion resident"
}
response=requests.patch("https://reqres.in/api/users/2",data=payload)
json_response=response.json()
assert json_response["name"]=="AP"
