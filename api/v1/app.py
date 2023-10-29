#!/usr/bin/python3                     """app.py to connect to API"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app_context(exception):
    """ teardown app context """
    storage.close()                    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)