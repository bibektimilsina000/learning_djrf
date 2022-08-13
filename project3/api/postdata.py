import requests
import json

url = "http://127.0.0.1:8000/api/create/"

data = {"name": "padam", "roll": 45, "city": "pokhara"}

jsondata = json.dumps(data)

r = requests.post(url=url, data=data)
