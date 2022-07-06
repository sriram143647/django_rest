import requests
import json

url = 'http://127.0.0.1:8000/crud_api/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,data=json_data)
    data = r.json()
    print(data)

# create record
def record_insert():
    data= {
        'uid': 105,
        'name':'priya',
        'mail':'priya.rai@gmail.com',
        'phone':'8566881104',
        'add1':'120 sardar nagar limbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(data)
    r = requests.post(url= url,data=j_data)
    data = r.json()
    print(data)
    
# update record
def partial_record_update():
    partial_data= {
        'uid': 104,
        'phone':'8866884401',
    }
    j_data = json.dumps(partial_data)
    r = requests.patch(url= url,data=j_data)
    data = r.json()
    print(data)

def full_record_update():
    full_data= {
        'uid': 104,
        'name':'rahul',
        'mail':'rahul@gmail.com',
        'phone':'9228238777',
        'add1':'120 sardar nagar limbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(full_data)
    r = requests.put(url= url,data=j_data)
    data = r.json()
    print(data)
    
def record_delete():
    partial_data= {'uid': 104}
    j_data = json.dumps(partial_data)
    r = requests.delete(url= url,data=j_data)
    data = r.json()
    print(data)
    
partial_record_update()
