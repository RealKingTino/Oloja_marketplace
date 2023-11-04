#!/usr/bin/python3
""" a module that contain forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TelField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """ a class that contain the login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    """a class for registration form"""
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    telephone = TelField('Telephone', validators=[DataRequired])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Login")