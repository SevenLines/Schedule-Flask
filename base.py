from flask import Flask
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from jinja_filters import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://disp:d7i7s7p@DATASCHEDULE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.jinja_env.filters['dayofweek'] = dayofweek
app.jinja_env.filters['parainfo'] = parainfo
app.jinja_env.filters['lesson_type_class'] = lesson_type_class
app.config['SECRET_KEY'] = 'ajkshedo mi1u02 301h2eih1 890yashkldj'

db = SQLAlchemy(app)

app.debug = True
toolbar = DebugToolbarExtension(app)