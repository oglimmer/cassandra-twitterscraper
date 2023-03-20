import requests, json

with open("conf.json") as c: conf = json.load(c)
REQUEST_URI = conf.get('API_url')
SECRET = conf.get('API_secret')
INSTANCE_NAME = conf.get('instance_name')
headers = {
    "AUTH": SECRET
}

def getTask():
    res = requests.get(f"{REQUEST_URI}/gettask", headers=headers)
    if res.status_code != 200: return None
    return res.json()

def commitTask(task, amount):
    task["tweets_scraped"] = amount
    res = requests.post(f"{REQUEST_URI}/submit", json=task, headers=headers)

def log(msg):
    tosend = {"msg": msg, "instance": INSTANCE_NAME}
    requests.post(f"{REQUEST_URI}/log", json=tosend, headers=headers)