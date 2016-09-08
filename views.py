import json
from flask.helpers import url_for
from itertools import groupby

from flask.templating import render_template
from flask.wrappers import Response
from flask import redirect, request

from base import app
from helpers import groups_json, auditories_json
from models import *


@app.route("/")
def index():
    print(Kontkurs.query.all())
    print(Auditory.query.all())
    return render_template("index.html", **{
        "groups_json": groups_json(),
        "auditories_json": auditories_json(),
    })


@app.route("/group/schedule/", methods=['POST'])
def group_schedule_redirect():
    kontgrp = request.form['kontgrp']
    return redirect(url_for("group_schedule", kont_id=kontgrp))


@app.route("/group/<kont_id>/schedule/")
def group_schedule(kont_id):
    group = Kontgrp.query.get(kont_id)
    raspis = Raspis.get_for_kontgrp(group)

    schedule = {
        para: {
            day: {
                'everyweek': None,
                'odd': None,
                'even': None,
            } for day in [1, 2, 3, 4, 5, 6]
            } for para in [0, 1, 2, 3, 4, 5, 6, 7, 8]
        }

    for lesson in raspis:
        if lesson.everyweek == 1:
            if lesson.day > 7:
                week = 'even'
            else:
                week = 'odd'
        else:
            week = 'everyweek'

        schedule[lesson.para][(lesson.day - 1) % 7 + 1][week] = lesson

    return render_template("groups/schedule.html", **{
        "group": group,
        "groups_json": groups_json(),
        "schedule": schedule
    })
