from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])







# future add on

class SearchForm():
    pass

class EmailForm():
    pass

