#!/usr/bin/python3
"""A module for the app_view"""
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = '83c76d379d999eae774e1bfe9bce0a08fbd50eed7066756787bc3dbbf1f63bc1'
from routes.app_routes import app_blueprint
from routes.auth_routes import auth_blueprint


app.register_blueprint(app_blueprint)
app.register_blueprint(auth_blueprint)

@app.errorhandler(404)
def not_found_error(error):
    """ 404 Not found
        -----
        return an error when page not found
    """
    return render_template('errors/404.html'), 404