from itertools import groupby

from flask.templating import render_template
from flask.wrappers import Response

from base import app
from models import *


@app.route("/")
def index():
    print(Kontkurs.query.all())
    print(Auditory.query.all())
    return "Hello World!"


@app.route("/group/<kont_id>/schedule/")
def group_schedule(kont_id):
    group = Kontgrp.query.get(kont_id)
    raspis = Raspis.get_for_kontgrp(group)

    schedule = {day: {
        para: list(lessons) for para, lessons in groupby(paras, lambda x: (x.para - 1) % 7 + 1)
    } for day, paras in groupby(raspis, lambda x: x.day)}

    return render_template("groups/schedule.html", **{
        "group": group,
        "schedule": schedule
    })