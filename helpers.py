import json
from flask import render_template

from models import Kontgrp, Auditory


def groups_json():
    return json.dumps([{"id": group.id, "text": group.title.strip()}
                       for group in Kontgrp.query.order_by(Kontgrp.title)], ensure_ascii=False)


def auditories_json():
    return json.dumps([{"id": auditory.id, "text": auditory.title.strip()}
                       for auditory in Auditory.query.order_by(Auditory.title)], ensure_ascii=False)


def render_template_schedule(template, **data):
    data.update({
        "groups_json": groups_json(),
        "auditories_json": auditories_json(),
    })
    return render_template(template, **data)