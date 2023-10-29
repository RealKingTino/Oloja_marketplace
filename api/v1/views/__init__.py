#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api")

from api.v1.views.login import *
from api.v1.views.signup import *
from api.v1.views.user_api import *
