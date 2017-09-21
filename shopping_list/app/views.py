from flask import render_template, flash, redirect, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    #Log in user
       
    return render_template("login.html")
    

@app.route('/checkUser', methods=['POST','GET'])
def checkUser():
    #Log in user
    email = request.form['email']
    password = request.form['password']
        
    if email and password:
        #Should check user credentials in database, meantime just open dashboard.html
        return (email + " " + password)

    else:
        return ('No values entered!!')

@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    #Create new user

    return render_template("new_Account.html")


@app.route('/createUser', methods=['POST','GET'])
def createUser():
    #Create user in database
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
        
    if firstname and lastname and address and phone and email and password:
        #Should check user credentials in database, meantime just open dashboard.html
        return (email + " " + password)

    else:
        return ('No values entered!!')
    

@app.route('/dashboard')
def dashBoard():
    #Display dashboard

    return render_template("dashboard.html")