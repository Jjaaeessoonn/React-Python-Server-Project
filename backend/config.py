# build api first
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) #init flask app; acts as objection-relational mapping
CORS(app) # allow cross-origin requests to app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #specify location of local sqlite db on machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) #crerate db instance that allows CRUD ops to sqlite db above

