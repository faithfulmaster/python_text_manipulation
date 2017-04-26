import datetime
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///newtutorial.db', echo=True)

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def do_sign():
    return render_template('registration.html')

@app.route('/registration', methods=['GET', 'POST'])
def do_reg():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    POST_FNAME = str(request.form['fname'])
    POST_LNAME = str(request.form['lname'])

    #create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(POST_USERNAME, POST_PASSWORD, POST_FNAME, POST_LNAME)
    session.add(user)

    session.commit()
    return home()

@app.route('/newcontact', methods=['POST'])
def create_contact():

    NAME = str(request.form['name'])
    ADDRESS = str(request.form['address'])
    CONTACT = str(request.form['contact'])
    

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=5000)
