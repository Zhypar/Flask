import requests
import json
r = requests.post("http://localhost:5000/register/", json={"username": "Alina", "password": "2222", "password2": "2222"})
print(r.text)
r = requests.post("http://localhost:5000/login/", json={"username": "Lina", "password": "2222", "password2": "2222"})
print(r.text)
r = requests.post("http://localhost:5000/register/", json={"username": "Alina", "password": "2222", "password2": "2222"})
print(r.text)