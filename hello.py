from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Stepic API.'

@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        user =  valid_login_user(request.form['username'], request.form['password'])
        if user != None:
            return 'success'
        else:
            return 'failed'
        
    else:
        return 'This is a login page.'
