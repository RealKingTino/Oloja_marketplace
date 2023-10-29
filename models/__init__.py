from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, text, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

app = Flask(__name__)

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
app.app_context().push()

from models import route
