from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
   
class NewUser(Form):
    email = StringField('email', validators=[DataRequired()])
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])   
    password = StringField('password', validators=[DataRequired()])