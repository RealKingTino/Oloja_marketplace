#!/usr/bin/python3
""" a module that contains the app routes"""
from flask import render_template, Blueprint

app_blueprint = Blueprint('app_blueprint', __name__, template_folder='templates')


@app_blueprint.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@app_blueprint.route('/details', strict_slashes=False)
def details():
    return render_template("market_details.html")

@app_blueprint.route('/product', strict_slashes=False)
def customer():
    return render_template("market.html")
