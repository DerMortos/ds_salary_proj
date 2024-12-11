import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": [5.1, 3.5, 1.4, 0.2]}

r = requests.post(URL,headers=headers, json=data)

print(r.json())