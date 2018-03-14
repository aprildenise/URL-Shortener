#__init__: creates/initializes the Flask instance from flask as well as the database 

#import the Flask class from flask
from flask import Flask 

#import sqlalchemy class
from flask_sqlalchemy import SQLAlchemy

#create an instance of the Flask class
app = Flask(__name__) 
app.config.from_pyfile('../config.py')

#create an instance of the SQLAlchemy class database using our flask instance
database = SQLAlchemy(app)

from views import *
