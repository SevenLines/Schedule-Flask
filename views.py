import json
from flask.helpers import url_for
from itertools import groupby

from flask.templating import render_template
from flask.wrappers import Response
from flask import redirect, request

from base import app
from helpers import groups_json, auditories_json, render_template_schedule
from models import *


@app.route("/")
def index():
    print(Kontkurs.query.all())
    print(Auditory.query.all())
    return render_template_schedule("index.html")


@app.route("/group/schedule/", methods=['POST'])
def group_schedule_redirect():
    kontgrp = request.form['kontgrp']
    return redirect(url_for("group_schedule", kont_id=kontgrp))

@app.route("/auditory/schedule/", methods=['POST'])
def auditory_schedule_redirect():
    auditory = request.form['auditory']
    return redirect(url_for("auditory_schedule", auditory_id=auditory))

@app.route("/auditory/<auditory_id>/schedule/")
def auditory_schedule(auditory_id):
    auditory = Auditory.query.get(auditory_id)
    raspis = Raspis.get_for_auditory(auditory)

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

    return render_template_schedule("groups/schedule.html", **{
        "auditory": auditory,
        "schedule": schedule
    })


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

    return render_template_schedule("groups/schedule.html", **{
        "group": group,
        "schedule": schedule
    })


@app.route("/teacher/<teacher_id>/schedule/")
def teacher_schedule(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    raspis = Raspis.get_for_teacher(teacher)

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

    return render_template_schedule("groups/schedule.html", **{
        "teacher": teacher,
        "schedule": schedule
    })