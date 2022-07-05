import requests

url = 'http://127.0.0.1:8000/std_info/102'
r = requests.get(url)
j_data = r.json()
print(j_data)