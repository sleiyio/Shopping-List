
class User(object):

    def __init__(self, firstname = "", lastname = "", email = "", password = ""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def changePassword(self, newPassword):
        #Change password
        self.password = newPassword

    def getFirstName(self):
        #View user name
        return (self.firstname)

    def getLastName(self):
        #View user name
        return (self.lastname)

    def getUserEmail(self):
        #View user email
        return self.email

    
