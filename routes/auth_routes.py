#!/usr/bin/python3
""" a module that contain the auth routes"""
from flask import flash, Blueprint, render_template
from forms import LoginForm

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates/auth')


@auth_blueprint.route('/login', method=['POST', 'GET'], strict_slashes=False)
def login():
    return render_template("auth/login.html", form=LoginForm())