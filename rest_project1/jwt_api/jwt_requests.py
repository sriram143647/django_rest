import requests
import json
header = {'content-Type':'application/json'}


# get token
def get_token():
    url = 'http://127.0.0.1:8000/get-jwttoken/'
    payload={
        'username': 'user1',
        'password': 'qwerty@user1'
    }
    payload = json.dumps(payload)
    res = requests.post(url=url,headers = header, data=payload)
    j_data = json.loads(res.text)
    print(j_data)
    
def verify_token():
    url = "http://127.0.0.1:8000/jwttoken-verify/"
    payload={'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyOTAyODQ2LCJpYXQiOjE2NzI5MDA5MjAsImp0aSI6IjY3MGFhOGViOGFhOTQ2NGNhYTJiZjU4MDAwMmIyMTUzIiwidXNlcl9pZCI6Mn0.4sBRbsOxj2NXUFgW-eoiJ3x0No_jNPwsQ79ldDiSJg0'}
    response = requests.request("POST", url, headers=header, data=payload)
    print(response.text)

def refersh_token():
    url = "http://127.0.0.1:8000/refresh-jwttoken/"
    payload={'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3Mjk4NzMyMCwiaWF0IjoxNjcyOTAwOTIwLCJqdGkiOiJhNjE4NDQ3ZWEzMmE0NTM4OGExNTIwOTQ0NzlmZDRlMCIsInVzZXJfaWQiOjJ9.bUS_pIaMthlzCsSS-LwWCaPu2yPXKi-ktzaEhRElLxc'}
    response = requests.request("POST", url, headers=header, data=payload)
    print(response.text)

def get_data(id=None):
    url = 'http://127.0.0.1:8000/jwt-data/'
    header = {
        'content-Type':'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyOTA0OTUyLCJpYXQiOjE2NzI5MDMyMDYsImp0aSI6IjQ0MDQ3OTU2ZjBjNDQ3MWY5MjQ5YzcxNTAxZjIzZGJlIiwidXNlcl9pZCI6Mn0.JNvme6kL62I8nXxX-SMwXJg6dkcR7eb8EgCMoqENyLE',
    }
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,headers = header, data=json_data)
    data = r.json()
    print(data)

get_data()