from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import csrf




app = Flask(__name__)

#csrf = csrf.CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasev2.db'
app.config['SECRET_KEY'] = 'e0569ac294edbcc15b7b82ee'
db = SQLAlchemy(app)

from HS3 import routes





