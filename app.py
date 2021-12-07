from os import uname
import re
from flask import Flask, app, request
from flask.templating import render_template
from models import *
from models import Userdata

# app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin')
def login():
    return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('register.html')

@app.route('/welcome', methods=["POST"])
def loginsucess():

    if request.method == "POST":
        uname = request.form.get('uname')
        password = request.form.get('psw')
        print(uname)
        print(password)
        return render_template('welcome.html',data = uname)


@app.route('/registrationsuccess', methods=["POST"])
def registration():

    if request.method == "POST":
        uname = request.form.get('uname')
        email = request.form.get('mail')
        password = request.form.get('psw')
        print(uname)
        print(email)
        print(password)
        return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True, port=3002)