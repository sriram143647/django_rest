import requests
import json

# get record
def fetch_data():
    url = 'http://127.0.0.1:8000/std_info/102'
    r = requests.get(url)
    j_data = r.json()
    print(j_data)

def get_data(id=None):
    url = 'http://127.0.0.1:8000/get_data/'
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,data=json_data)
    data = r.json()
    print(data)

# create record
def record_insert():
    url = 'http://127.0.0.1:8000/rec_create/'
    data= {
        'uid': 17,
        'name':'rahul',
        'mail':'rahul@gmail.com',
        'phone':'9228327007',
        'add1':'25 maruti nagar linbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(data)
    r = requests.post(url= url,data=j_data)
    data = r.json()
    print(data)
    
# update record
def record_update():
    url = 'http://127.0.0.1:8000/rec_create/'
    data= {
        'uid': 104,
        'name':'rahul',
        'mail':'rahul@yahoo.com',
        'phone':'9228327007',
        'add1':'25 maruti nagar linbayat',
        'add2':'udhna',
        'city':'surat',
    }
    j_data = json.dumps(data)
    r = requests.put(url= url,data=j_data)
    data = r.json()
    print(data)
    
record_insert()