from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, DateTime, text, Integer
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oloja.db'
db = SQLAlchemy(app)
app.app_context().push()
from models import route