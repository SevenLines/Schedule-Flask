from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from jinja_filters import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://disp:d7i7s7p@DATASCHEDULE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.jinja_env.filters['dayofweek'] = dayofweek
app.jinja_env.filters['parainfo'] = parainfo

db = SQLAlchemy(app)
