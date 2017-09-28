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

class NewShoppingList(Form):
    shoppinglistname = StringField('shoppinglistname', validators=[DataRequired()])
    itemdescription1 = StringField('itemdescription1', validators=[DataRequired()])
    itemdquantity1 = StringField('itemdquantity1', validators=[DataRequired()])
    itemdescription2 = StringField('itemdescription2', validators=[DataRequired()])
    itemdquantity2 = StringField('itemdquantity2', validators=[DataRequired()])
    itemdescription3 = StringField('itemdescription3', validators=[DataRequired()])
    itemdquantity3 = StringField('itemdquantity3', validators=[DataRequired()])