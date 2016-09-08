import json

from models import Kontgrp, Auditory


def groups_json():
    return json.dumps([{"id": group.id, "text": group.title}
                       for group in Kontgrp.query.order_by(Kontgrp.title)])


def auditories_json():
    return json.dumps([{"id": auditory.id, "text": auditory.title}
                       for auditory in Auditory.query.order_by(Auditory.title)])
