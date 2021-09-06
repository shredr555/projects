from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("Remember me")


class RegisterForm(FlaskForm):
    email = StringField("Email: ", validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField("Username: ", validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators=[InputRequired(), Length(min=8, max=80)])
