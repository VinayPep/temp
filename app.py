from os import uname
import re
from flask import Flask, app, request
from flask.templating import render_template
from models import *
from models import Userdata
import hashlib
g_name = ""


# app = Flask(__name__)
# 
@app.route('/test')
def test():
    return render_template('index.html')

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
        # print(uname)
        # print(password)
        global g_name
        g_name = uname
        print(g_name)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(Userdata).filter(Userdata.uname==uname, Userdata.password==hashedPassword)
        return render_template('welcome.html',data = uname)


@app.route('/registrationsuccess', methods=["POST"])
def registration():

    if request.method == "POST":
        uname = request.form.get('uname')
        email = request.form.get('mail')
        password = request.form.get('psw')
        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = Userdata(uname = uname,email = email,password = hashedPassword)
        db.session.add(entry)
        db.session.commit()
        return render_template('login.html')

@app.route('/personal')
def searchpersonal():
    global g_name
    return render_template('personal.html',data = g_name)


@app.route('/group')
def searchall():
    global g_name
    return render_template('group.html',data = g_name)


if __name__ == "__main__":
    app.run(debug=True, port=4001)
    



# ALTER TABLE users ADD COLUMN id SERIAL PRIMARY KEY 