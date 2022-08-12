import requests

URL = "http://127.0.0.1:8000/api/stu/"

data = requests.get(URL)

data = data.json()

print(data)
