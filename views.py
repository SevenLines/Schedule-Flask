import json

import flask
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
    return render_template_schedule("index.html")


@app.route("/group/schedule/", methods=['POST'])
def group_schedule_redirect():
    kontgrp = request.form['kontgrp']
    return redirect(url_for("group_schedule", kont_id=kontgrp))


@app.route("/auditory/schedule/", methods=['POST'])
def auditory_schedule_redirect():
    auditory = request.form['auditory']
    return redirect(url_for("auditory_schedule", auditory_id=auditory))


@app.route("/teacher/schedule/", methods=['POST'])
def teacher_schedule_redirect():
    teacher = request.form['teacher']
    return redirect(url_for("teacher_schedule", teacher_id=teacher))


@app.route("/auditory/<auditory_id>/schedule/")
def auditory_schedule(auditory_id):
    auditory = Auditory.query.get(auditory_id)
    schedule = Raspis.get_for_auditory(auditory)

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "auditory": auditory,
        "schedule": schedule
    })


@app.route("/group/<kont_id>/schedule/")
def group_schedule(kont_id):
    group = Kontgrp.query.get(kont_id)
    if group:
        schedule = Raspis.get_for_kontgrp(group)
    else:
        group = Kontkurs.query.get(kont_id)
        schedule = Raspis.get_for_kontkurs(group)

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "group": group,
        "schedule": schedule
    })


@app.route("/teacher/<teacher_id>/schedule/")
def teacher_schedule(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    schedule = Raspis.get_for_teacher(teacher)

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "teacher": teacher,
        "schedule": schedule
    })


@app.route("/discipline/<discipline_id>/schedule/")
def discipline_schedule(discipline_id):
    discipline = Discipline.query.get(discipline_id)
    schedule = Raspis.get_for_discipline(discipline)

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "discipline": discipline,
        "schedule": schedule
    })

@app.route("/report/physical-education-schedule/")
def physical_education_schedule():
    """
    расписание физической культуры
    :return:
    """
    PHYSICAL_EDUCATION_CHAIR_ID = 218
    chair = Chair.query.get(PHYSICAL_EDUCATION_CHAIR_ID)
    schedule = Raspis.get_for_chair(chair, group_by_lesson=True, key_template='{discipline_id}_{nt}_{fac_id}')

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "schedule": schedule
    })

@app.route("/report/foreign-for-humans/")
def foreign_for_humans():
    """
    расписание иностранных для гуманитарных специальностей
    :return:
    """
    FOREIGN_HUMAN_CHAIR_ID = 366
    chair = Chair.query.get(FOREIGN_HUMAN_CHAIR_ID)
    schedule = Raspis.get_for_chair(chair, group_by_lesson=True, key_template='{discipline_id}_{nt}_{fac_id}')

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "schedule": schedule
    })

@app.route("/report/foreign-for-tech-1/")
def foreign_for_tech_1():
    """
    расписание иностранных для гуманитарных специальностей
    :return:
    """
    FOREIGN_TECH_CHAID_ID = 216
    chair = Chair.query.get(FOREIGN_TECH_CHAID_ID)
    schedule = Raspis.get_for_chair(chair, group_by_lesson=True, key_template='{discipline_id}_{nt}_{fac_id}')

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "schedule": schedule
    })

@app.route("/report/foreign-for-tech-2/")
def foreign_for_tech_2():
    """
    расписание иностранных для гуманитарных специальностей
    :return:
    """
    FOREIGN_TECH_CHAID_ID = 217
    chair = Chair.query.get(FOREIGN_TECH_CHAID_ID)
    schedule = Raspis.get_for_chair(chair, group_by_lesson=True, key_template='{discipline_id}_{nt}_{fac_id}')

    if request.is_xhr:
        return flask.jsonify(schedule)

    return render_template_schedule("groups/schedule.html", **{
        "schedule": schedule
    })