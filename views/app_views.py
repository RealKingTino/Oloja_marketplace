#!/usr/bin/python3
"""A module for the app_view"""
from flask import Flask
app = Flask(__name__)
from routes.app_routes import app_blueprint
from routes.auth_routes import auth_blueprint


app.register_blueprint(app_blueprint)
app.register_blueprint(auth_blueprint)
