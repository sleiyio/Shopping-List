from app import db

class user(object):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    address = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, firstname = "", lastname = "", address = "", email = "", password = ""):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.password = password

    def addUser(self, item, quantity):
        #Write user details to database
        db.session.add(self)
        db.session.commit()

    def editUserAddress(self, newAddress):
        #Edit address
        self.address = newAddress

    def changePassword(self, newPassword):
        #Change password
        self.password = newPassword

    def viewUserName(self):
        #View user name
        return (self.firstname + ' ' + self.lastname)

    def viewUserAddress(self):
        #View user address
        return self.address

    def viewUserEmail(self):
        #View user email
        return self.email

    
