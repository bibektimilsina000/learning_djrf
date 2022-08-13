import requests
import json

url = "http://127.0.0.1:8000/api/create/"

data = {"name": "krishna", "roll": 95, "city": "begnas"}

jsondata = json.dumps(data)

headers = {"Content-Type": "application/json"}

response = requests.post(url=url, data=jsondata, headers=headers)
print(response.json())
