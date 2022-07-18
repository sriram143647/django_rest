import requests
import json

url = 'http://127.0.0.1:8000/api2/'
header = {'content-Type':'application/json'}

def record_fetch(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,headers = header, data=json_data)
    data = r.json()
    print(data)

# create record
def record_insert():
    data= {
        'uid': 103,
        'name':'rahul',
        'mail':'rahul.chauhan@gmail.com',
        'phone':'8523811104',
        'add1':'120 sardar nagar limbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(data)
    r = requests.post(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
# update record
def partial_record_update():
    partial_data= {
        'uid': 103,
        'phone':'8866884401',
    }
    j_data = json.dumps(partial_data)
    r = requests.patch(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)

def full_record_update():
    full_data= {
        'uid': 103,
        'name':'virat',
        'mail':'virat.solanki@gmail.com',
        'phone':'9228238777',
        'add1':'15 maruti nagar limbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(full_data)
    r = requests.put(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
def record_delete():
    partial_data= {'uid': 103}
    j_data = json.dumps(partial_data)
    r = requests.delete(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
partial_record_update()