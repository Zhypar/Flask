from flask import Flask, request
import json 
import requests
app = Flask(__name__)
data = dict()
l_data = dict()


@app.route('/register/', methods=['POST'])
def register_user():
    data = json.loads(request.data.decode())
    username = data.get("username")
    password = data.get("password")
    password2 = data.get("password2")
    if password != password2:
        return "Passwords don't match"
    elif username == l_data.get("username"):
        return "This name is already taken"
    else:
        l_data.update(data)
        return "Succesfully registered!"
    


@app.route('/login/', methods=['POST'])
def login_user():
    l_data = json.loads(request.data.decode())
    if data.get("username") != l_data.get("username"):
        return "User does not exist"
    return "Hello!"
    

if __name__ == '__main__':
    app.run()
