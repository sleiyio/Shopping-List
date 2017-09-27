from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm, NewUser

users = {}

@app.route('/')
@app.route('/index')
def index():
    #Log in user       
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    #Log in user    
    form = LoginForm()
    if form.is_submitted:
        #Check if the user exists
        return_value = checkUser(form)
        if return_value:
            return redirect('/dashboard')
        
    return render_template('login.html')

def checkUser(form):
    #Check if user exists    
    email = form.email.data
    password = form.password.data
    
    for k, v in users.items():
        if email == users[k].get('email') and password == users[k].get('pwd'):
            #Credentials match, log in successfull
            return True
    
    return False
    

@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    #Create new user    
    form = NewUser() 
    if form.is_submitted: 
              
        return_value = createUser(form)
        if return_value:
            return redirect('/login')

    return render_template('new_account.html',
                            title='New Account',
                            form=form)

def createUser(form):
    #Create user in database
    firstname = form.firstname.data
    lastname = form.lastname.data
    email = form.email.data
    password = form.password.data
    
    if firstname and lastname and email and password:
        userNo = len(users) + 1
        users[userNo] = {'fname' : firstname, 'lname' : lastname, 'email' : email, 'pwd' : password}
        return True
    else:
        return False


@app.route('/dashboard')
def dashBoard():
    #Display dashboard
    return render_template("dashboard.html")

