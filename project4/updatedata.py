import json
import requests


url = "http://127.0.0.1:8000/api/stu/"


def getData(id=None):
    data = {}

    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    r = requests.get(url=url, data=json_data, headers=headers)

    data = r.json()
    print(data)


getData()


def post_data():

    data = {"name": "bimal", "roll": 498, "city": "panpauti"}

    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"}

    r = requests.post(url=url, data=json_data, headers=headers)

    data = r.json()
    print(data)


# post_data()
