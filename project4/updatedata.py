import json
import requests


url = "http://127.0.0.1:8000/api/stu"


def getData(id=None):
    data = {}

    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)

    data = r.json()
    print(data)


# getData(2)


def post_data():

    data = {"name": "kamal", "roll": 423, "city": "rachi"}

    json_data = json.dumps(data)

    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


post_data()
