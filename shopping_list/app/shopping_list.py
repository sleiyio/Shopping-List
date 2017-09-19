
from flask import Flask, render_template, json, request
app = Flask(__name__)

#default home page - index.html
@app.route('/')
def main():
    return render_template('index.html')

#Log in page
@app.route('/index')
def showIndex():
    return render_template('index.html')

#New user to create create account
@app.route('/createAccount')
def showSignUp():
    return render_template('new_account.html')

#Create account once user clicks "Create Account" button
@app.route('/newAccount', methods=['POST'])
def newAccount(): 
    
    # get the values keyed in by user
    firstname = "John"#request.form['firstName']
    lastname = "Doe"#request.form['lastName']
    address = "123"#request.form['address']
    email = "johndoe@gmail.com"#request.form['email']
    phone = "0722698553"#request.form['phone']
    password = "xyz"#request.form['password']
    repeatpassword = "xyz"#request.form['repeat_password']
       
     # validate the user input
    if firstname and lastname and address and email and phone and password and repeatpassword:
        #return json.dumps({'html':'<span>All fields have been completed. Ready to create user !!</span>'})
        return render_template('index.html')
    else:
        return json.dumps({'html':'<span>Please complete all the fields</span>'})
    

#Dashboard page
@app.route('/dashboard')
def showDashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
