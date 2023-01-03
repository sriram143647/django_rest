from lib2to3.pgen2 import token
import requests
import json
header = {'content-Type':'application/json'}


# get token
def get_token():
    url = 'http://127.0.0.1:8000/get-token/'
    payload={
        'username': 'user1',
        'password': 'qwerty@user1'
    }
    payload = json.dumps(payload)
    res = requests.post(url=url,headers = header, data=payload)
    print(res.text)

def get_data(id=None):
    url = 'http://127.0.0.1:8000/api4/'
    header = {
        'content-Type':'application/json',
        'Authorization': 'Token 3c687291ae06cf325db1ecba2e20c3a48c34436a',
    }
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,headers = header, data=json_data)
    data = r.json()
    print(data)
    
get_data()