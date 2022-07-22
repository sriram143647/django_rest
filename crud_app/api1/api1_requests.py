import requests
import json

url = 'http://127.0.0.1:8000/api1/'
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
        'name':'rahul',
        # 'mail':'rahul.chauhan@gmail.com',
        'phone':'8523811104',
        'add':'120 sardar nagar limbayat',
    }
    j_data = json.dumps(data)
    r = requests.post(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
def full_record_update():
    full_data= {
        'id':2,
        'name':'virat',
        'mail':'virat.solanki@gmail.com',
        'phone':'9228238777',
        'add':'15 maruti nagar limbayat',
    }
    j_data = json.dumps(full_data)
    r = requests.put(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
def record_delete():
    partial_data= {'id': 2}
    j_data = json.dumps(partial_data)
    r = requests.delete(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)

def start():
    print('select the operations')
    print('Fetch Records')
    print('Insert Record')
    print('Update Record')
    print('Delete Record')
    ch = input(print('Enter your Choice:'))
    print(ch)

start()