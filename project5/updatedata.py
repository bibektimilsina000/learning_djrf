# just a front app
import json
import requests


url = "http://127.0.0.1:8000/api/stu/"
headers = {"Content-Type": "application/json"}


def getData(id=None):
    data = {}

    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)

    r = requests.get(url=url, data=json_data, headers=headers)

    data = r.json()
    print(data)


getData()


def post_data():

    data = {"name": "pandey kumar yadav", "roll": 78, "city": "rampur"}

    json_data = json.dumps(data)

    r = requests.post(url=url, data=json_data, headers=headers)

    data = r.json()
    print(data)


# post_data()


def updateData():
    data = {
        "id": 3,
        "name": "sapana",
        "city": "chorbasti",
    }

    json_data = json.dumps(data)

    r = requests.put(url=url, data=json_data, headers=headers)
    data = r.json()
    print(data)


# updateData()


def deleteData():

    data = {"id": 3}

    json_data = json.dumps(data)

    r = requests.delete(url=url, data=json_data, headers=headers)
    data = r.json()

    print(data)


# deleteData()
