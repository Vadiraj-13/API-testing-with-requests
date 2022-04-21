import requests

response=requests.delete("https://reqres.in/api/users/2")
print(response)
assert response.status_code==204