#!/usr/bin/python3
""" a module that contain the auth routes"""
from flask import flash, Blueprint, render_template, request, abort, jsonify, redirect, sessions
from forms import LoginForm
import requests
auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates/auth')


@auth_blueprint.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """ Login
        ------
        return an entry point to the user dashboard
    """
    return render_template("auth/login.html", form=LoginForm())


@auth_blueprint.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth():
    """ auth
        ----
        auth to the server
    """
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    url = 'http://api.v1.dev.localhost:5000/signin'
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response = response.json()
        sessions.details = response
        redirect('/dashboard')
    abort(401, 'Unauthorized')