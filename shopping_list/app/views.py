from flask import flash, redirect, render_template, request
from app import app
from .forms import LoginForm, NewUser, NewShoppingList
from app.user import User

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
            user = {'name': form.email.data}            
            return render_template('dashboard.html', user=user)
        
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

    #newUser = User(firstname, lastname, email, password)
    
    if firstname and lastname and email and password:
        userNo = len(users) + 1
        users[userNo] = {'fname' : firstname, 'lname' : lastname, 'email' : email, 'pwd' : password} #newUser
        return True
    else:
        return False


@app.route('/dashboard')
def dashBoard():
    #Display dashboard
    form = NewShoppingList()
    if form.is_submitted:
        return_value = updateShoppingList(form)
        if return_value:
            return redirect('/dashboard')

    return render_template("dashboard.html")


def updateShoppingList(form):
    #Update shopping list with items supplied by user
    shoppinglistname = ""
    itemdescription1 = form.itemdescription1
    itemdquantity1 = form.itemdquantity1
    itemdescription2 = form.itemdescription2
    itemdquantity2 = form.itemdquantity2
    itemdescription3 = form.itemdescription3
    itemdquantity3 = form.itemdquantity3

    return 1

