import json
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

    # schedule = {para: {
    #     day: list(lessons) for day, lessons in groupby(paras, lambda x: x.para)
    # } for para, paras in groupby(raspis, lambda x: (x.day - 1) % 7 + 1)}

    schedule = {
        para: {
            day: {
                'everyweek': None,
                'odd': None,
                'even': None,
            } for day in [1,2,3,4,5,6]
        } for para in [0, 1,2,3,4,5,6,7,8]
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
        "groups_json": json.dumps([{"id": group.id, "text": group.title}
                              for group in Kontgrp.query.order_by(Kontgrp.title)]),
        "schedule": schedule
    })