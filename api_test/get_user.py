import requests

resp=requests.get("https://reqres.in/api/users?page=2")
json_resp=resp.json()
print(json_resp["data"][0]["first_name"])
assert (json_resp["data"][0]["first_name"]).endswith("el"),"Name is not matching"
headers=resp.headers
print(headers)