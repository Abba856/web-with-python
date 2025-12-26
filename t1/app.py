import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)

res = json.loads(response.text)

for data in res:
    print(data)