import requests
import json
url = "http://httpbin.org/post"
header={"Content-Type":"application/json"}

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload,headers=header)
print(r.text)


r = requests.post(url=url,headers=header,data=payload)
print(r.json())