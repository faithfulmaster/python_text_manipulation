from __future__ import print_function
import datetime
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, abort, url_for
from flask import session as se
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import requests
import sys


engine = create_engine('sqlite:///newtutorial.db', echo=True)

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def do_sign():
    return render_template('registration.html')

@app.route('/showcontact', methods=['GET', 'POST'])
def dispcontact():

    if se.get('logged_in') == True:

        Session = sessionmaker(bind=engine)
        s = Session()
        Username = se['name']

        query = s.query(User.id1).filter(User.username.in_([Username]))
        result = query.first()

        if result:
            local = result[0]
            query = s.query(Contact).filter(Contact.local_id.in_([local]))
            result = query.all()
            if result:
                return render_template('dispcontact.html', cont=result)

        return home()

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

@app.route('/newcontact', methods=['GET', 'POST'])
def create_contact():


    NAME = str(request.form['name'])
    ADDRESS = str(request.form['address'])
    CONTACT = str(request.form['contact'])

    if se.get('logged_in') == True:

        Session = sessionmaker(bind=engine)
        s = Session()
        Username = se['name']

        query = s.query(User.id1).filter(User.username.in_([Username]))
        result = query.first()

        if result:
            local_id = result[0]
            contact = Contact(local_id, NAME, ADDRESS, CONTACT)
            s.add(contact)
            s.commit()
            return home()
        else:
            return redirect(url_for('logout'))

@app.route('/')
def home():
    sumSessionCounter()
    if not se.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    sumSessionCounter()
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        se['name'] = POST_USERNAME
        se['logged_in'] = True
        return render_template('contact.html')
    else:
        flash('wrong password!')
        return home()

def sumSessionCounter():
  try:
    se['counter'] += 1
  except KeyError:
    se['counter'] = 1

@app.route("/logout")
def logout():
    se.clear()
    se['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='127.0.0.1', port=5000)
