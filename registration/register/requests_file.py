import requests
import json

url = 'http://127.0.0.1:8000/api1/'
header = {'content-Type':'application/json'}

# record fetch
def record_fetch():
    mail = input('Enter mail:')
    if mail is not None:
        data = {'email':mail}
    else:
        data = {'email':None}
    json_data = json.dumps(data)
    r = requests.get(url=url,headers = header, data=json_data)
    data = r.json()
    print(data)

# create record
def record_insert():
    name = input('Enter name:')
    mail = input('Enter mail:')
    phone = input('Enter phone:')
    add = input('Enter address:')
    gender = input('Enter Gender (M/F):')
    data= {
        'name':name,
        'email':mail,
        'phone':phone,
        'add':add,
        'gneder':gender.upper()
    }
    j_data = json.dumps(data)
    r = requests.post(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)

# record_update    
def record_update():
    name = input('Enter name:')
    mail = input('Enter mail:')
    phone = input('Enter phone:')
    add = input('Enter address:')
    gender = input('Enter Gender (M/F):')
    data= {
        'name':name,
        'email':mail,
        'phone':phone,
        'add':add,
        'gneder':gender
    }
    j_data = json.dumps(data)
    r = requests.put(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)
    
# record delete
def record_delete():
    mail = input('Enter mail:')
    data = {'email':mail}
    j_data = json.dumps(data)
    r = requests.delete(url=url,headers = header, data=j_data)
    data = r.json()
    print(data)

def start():
    print('Select the operations')
    print('1. Record Fetch')
    print('2. Record Insert')
    print('3. Record Update')
    print('4. Record Delete')
    ch = int(input('Enter your choice:'))
    if ch == 1:
        record_fetch()
    elif ch==2:
        record_insert()
    elif ch==3:
        record_update()
    elif ch==4:
        record_delete()
    
start()