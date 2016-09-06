from base import app
from models import *


@app.route("/")
def index():
    print(Kontkurs.query.all())
    print(Auditory.query.all())
    return "Hello World!"
